#!/usr/bin/env python3
"""Score one Meta ads round against the ladder and our targets.

Usage:
  python3 scripts/ladder.py companies/<company>/campaigns/<round>
  python3 scripts/ladder.py --scoreboard companies

What it does:
  1. Reads campaign.json (the plan, the goal, hand-typed numbers) and pulled.json
     (the numbers Claude pulled from the Meta Ads connector) in the round folder.
  2. Adds the hand numbers from campaign.json "manual". Hand numbers win.
  3. Colors health lights and every step red / yellow / green using targets.json.
  4. Scores every ad and every placement, so blended numbers can't hide a leak.
  5. Finds the biggest leak and says what to fix next.
  6. Compares to the baseline round, if there is one.
  7. Writes results.md in the round folder and rebuilds companies/SCOREBOARD.md.

Why pulled.json and not a live API call: the Meta numbers come from the Meta Ads
connector in the chat (Claude writes pulled.json, see LOOP.md). The access token never
lives in this repo. Only uses the Python standard library (Python 3.8+).
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TARGETS = json.loads((REPO / "targets.json").read_text())
RULES = TARGETS["rules"]

DOT = {"green": "🟢", "yellow": "🟡", "red": "🔴", "early": "⚪", "none": "·", "odd": "🟣"}
WORD = {"green": "good", "yellow": "average", "red": "fix", "early": "too early",
        "none": "no data", "odd": "check: too good to be real"}
COUNT_KEYS = ["spend", "impressions", "reach", "clicks", "hooked", "thruplays",
              "installs", "trials", "paid", "conversations", "qualified", "sales",
              "leads", "booked", "won"]


# ---------------------------------------------------------------- loading

def load_json(path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text())


def num(v):
    """Numbers from the connector arrive as strings, dicts ({value, unit}) or null."""
    if v is None or v == "":
        return None
    if isinstance(v, dict):
        v = v.get("value")
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def add(a, b):
    if a is None and b is None:
        return None
    return (a or 0) + (b or 0)


def numbers_for(folder):
    """Totals for the round: pulled totals (or the sum of the ads), then hand numbers."""
    camp = load_json(folder / "campaign.json")
    if camp is None:
        sys.exit(f"No campaign.json in {folder}")
    pulled = load_json(folder / "pulled.json", {}) or {}
    ads = pulled.get("ads") or []
    placements = pulled.get("placements") or []

    n = {k: None for k in COUNT_KEYS}
    totals = pulled.get("totals") or {}
    for ad in ads:
        for k in COUNT_KEYS:
            if k != "reach":  # reach doesn't add up across ads
                n[k] = add(n[k], num(ad.get(k)))
    for k, v in totals.items():  # campaign-level numbers from Meta win over the sum
        if k in COUNT_KEYS and num(v) is not None:
            n[k] = num(v)
    n["frequency"] = num(totals.get("frequency"))
    if n["frequency"] is None and n["impressions"] and n["reach"]:
        n["frequency"] = n["impressions"] / n["reach"]

    manual = camp.get("manual") or {}
    for k, v in manual.items():
        if v is not None:
            n[k] = v
    # Hook rate only makes sense over video ads: count impressions of ads that have video plays.
    video_imp = [num(ad.get("impressions")) or 0 for ad in ads if num(ad.get("hooked")) is not None]
    n["video_impressions"] = sum(video_imp) if video_imp else None
    n["_pulled_at"] = pulled.get("pulled_at")
    n["_hooked_metric"] = pulled.get("hooked_metric")
    return camp, n, ads, placements


# ---------------------------------------------------------------- lights

def ratio(top, bottom):
    if top is None or not bottom:
        return None
    return top / bottom


def light(value, t, den=None):
    """Color a value against one target. Returns (color, value)."""
    if value is None:
        return "none"
    if den is not None and t.get("min_den") and den < t["min_den"]:
        return "early"
    if t.get("suspicious_over") is not None and value > t["suspicious_over"]:
        return "odd"
    if t["better"] == "higher":
        if value >= t["green"]:
            return "green"
        if value < t["red"]:
            return "red"
    else:
        if value <= t["green"]:
            return "green"
        if value >= t["red"]:
            return "red"
    return "yellow"


def pct(v, digits=1):
    return "—" if v is None else f"{v * 100:.{digits}f}%"


def money(v, cur="USD"):
    if v is None:
        return "—"
    sign = "$" if cur == "USD" else ""
    tail = "" if cur == "USD" else f" {cur}"
    return f"{sign}{v:,.2f}{tail}"


def count(v):
    return "—" if v is None else f"{v:,.0f}"


def health_lights(n, placements):
    out = []
    h = TARGETS["health"]
    out.append(("frequency", n.get("frequency"), light(n.get("frequency"), h["frequency"]), "x"))
    rej = n.get("rejected_ads")
    out.append(("rejected_ads", rej, light(rej, h["rejected_ads"]) if rej is not None else "none", "n"))
    ll = n.get("learning_limited")
    ll_val = None if ll is None else (1 if ll else 0)
    out.append(("learning_limited", ll_val, light(ll_val, h["learning_limited"]) if ll_val is not None else "none", "yesno"))
    an = an_click_share(placements)
    out.append(("audience_network_clicks", an, light(an, h["audience_network_clicks"]), "%"))
    return out


def an_click_share(placements):
    total = sum(num(p.get("clicks")) or 0 for p in placements)
    if not total:
        return None
    an = sum(num(p.get("clicks")) or 0 for p in placements
             if str(p.get("platform", "")).startswith("audience_network"))
    return an / total


def fmt_health(key, value, kind):
    if value is None:
        return "—"
    if kind == "%":
        return pct(value)
    if kind == "x":
        return f"{value:.2f}x"
    if kind == "yesno":
        return "yes" if value else "no"
    return f"{value:.0f}"


# ---------------------------------------------------------------- the round

def score_round(folder):
    camp, n, ads, placements = numbers_for(folder)
    goal_key = camp.get("goal") or "app_subscriptions"
    if goal_key not in TARGETS["goals"]:
        sys.exit(f"Unknown goal '{goal_key}'. Pick one of: {', '.join(TARGETS['goals'])}")
    goal = TARGETS["goals"][goal_key]
    cur = camp.get("currency") or "USD"

    handoffs = []
    for key, t in goal["handoffs"].items():
        top, bottom = n.get(t["num"]), n.get(t["den"])
        value = ratio(top, bottom)
        handoffs.append({"key": key, "t": t, "value": value, "den": bottom,
                         "light": light(value, t, bottom)})

    creative = []
    for key, t in TARGETS["creative"].items():
        den_key = "video_impressions" if t["den"] == "impressions" else t["den"]
        top, bottom = n.get(t["num"]), n.get(den_key)
        value = ratio(top, bottom)
        creative.append({"key": key, "t": t, "value": value, "den": bottom,
                         "light": light(value, t, bottom)})

    health = health_lights(n, placements)
    spend = n.get("spend")
    score_n = n.get(goal["score"])
    early_n = n.get(goal["early_signal"])

    days_since_change = None
    if camp.get("last_change"):
        days_since_change = (dt.date.today() - dt.date.fromisoformat(camp["last_change"])).days

    return {
        "camp": camp, "n": n, "ads": ads, "placements": placements, "goal_key": goal_key,
        "goal": goal, "cur": cur, "handoffs": handoffs, "creative": creative, "health": health,
        "spend": spend, "score_n": score_n, "early_n": early_n,
        "cost_score": ratio(spend, score_n), "cost_early": ratio(spend, early_n),
        "days_since_change": days_since_change,
    }


def fix_next(r):
    reds = [h for h in r["health"] if h[2] == "red"]
    if reds:
        names = ", ".join(TARGETS["health"][h[0]]["label"] for h in reds)
        fixes = " ".join(TARGETS["health"][h[0]]["fix"] for h in reds)
        return f"**Setup first:** {names}. {fixes} Don't judge creatives until this is green."
    odd = [h for h in r["handoffs"] if h["light"] == "odd"]
    if odd:
        h = odd[0]
        return (f"**{h['t']['label']} is too high to be real ({pct(h['value'])}).** "
                "Check placements and tracking before trusting any step below it.")
    judged = [h for h in r["handoffs"] if h["light"] in ("red", "yellow")]
    for h in judged:  # funnel order: the first red step is the leak
        if h["light"] == "red":
            return f"**{h['t']['label']}** ({pct(h['value'])}, red under {pct(h['t']['red'], 0)}). {h['t']['fix']}"
    if judged:
        worst = min(judged, key=lambda h: h["value"] / h["t"]["green"])
        return f"**{worst['t']['label']}** ({pct(worst['value'])}, green at {pct(worst['t']['green'], 0)}). {worst['t']['fix']}"
    if any(h["light"] == "green" for h in r["handoffs"]):
        return "Every judged step is green. Next: bring a new challenger creative to beat the control."
    return "Too early: no step has enough people to judge yet."


def ad_hint(ad, target_cost, early_key, cur):
    imp = num(ad.get("impressions")) or 0
    spend = num(ad.get("spend")) or 0
    results = num(ad.get(early_key)) or 0
    if target_cost:
        if results == 0 and spend >= RULES["kill_after_spend_multiple"] * target_cost:
            return f"kill candidate: {money(spend, cur)} spent, no results"
    if imp < RULES["min_impressions_to_judge_ad"]:
        return "too early"
    if not target_cost:
        return "set target cost to judge"
    cost = spend / results if results else None
    if cost is not None and cost <= target_cost:
        return "winner candidate"
    if cost is not None and cost <= 1.5 * target_cost:
        return "keep watching"
    return "losing"


def write_results(folder, r):
    camp, n, goal, cur = r["camp"], r["n"], r["goal"], r["cur"]
    early_key, score_key = goal["early_signal"], goal["score"]
    labels = dict(goal["steps"])
    L = []
    L.append(f"# Results: {camp.get('company')} · {camp.get('name')}")
    L.append("")
    L.append(f"Scored {dt.date.today().isoformat()} by scripts/ladder.py. Don't edit by hand; rerun the script.")
    L.append(f"Numbers pulled from Meta: {n.get('_pulled_at') or 'never (hand numbers only)'}. "
             f"Goal: **{goal['label']}**. Targets version {TARGETS['version']}.")
    L.append("")

    d = r["days_since_change"]
    if d is not None and d < RULES["wait_days_after_change"]:
        L.append(f"> ⚪ **Too early to call a verdict.** Day {d} of {RULES['wait_days_after_change']} "
                 "since the last change. Meta is still learning; watch health lights only.")
        L.append("")

    L.append("## The score")
    L.append("")
    L.append("| What | Count | Cost each |")
    L.append("|---|---:|---:|")
    L.append(f"| **{labels[score_key]}** (the score) | **{count(r['score_n'])}** | **{money(r['cost_score'], cur)}** |")
    L.append(f"| {labels[early_key]} (early signal) | {count(r['early_n'])} | {money(r['cost_early'], cur)} |")
    L.append(f"| Spend | {money(r['spend'], cur)} | |")
    L.append("")

    L.append("## Health lights (stop if red)")
    L.append("")
    L.append("| Light | Now | Green | Red | |")
    L.append("|---|---:|---:|---:|---|")
    for key, value, col, kind in r["health"]:
        t = TARGETS["health"][key]
        g = fmt_health(key, t["green"], kind) if kind != "yesno" else "no"
        rd = fmt_health(key, t["red"], kind) if kind != "yesno" else "yes"
        L.append(f"| {t['label']} | {fmt_health(key, value, kind)} | {g} | {rd} | {DOT[col]} {WORD[col]} |")
    L.append("")

    L.append("## The ladder")
    L.append("")
    L.append("| Step | People | Handoff | Rate | Green at | |")
    L.append("|---|---:|---|---:|---:|---|")
    hmap = {h["t"]["num"]: h for h in r["handoffs"]}
    for key, label in goal["steps"]:
        h = hmap.get(key)
        if h:
            L.append(f"| {label} | {count(n.get(key))} | {h['t']['label']} | {pct(h['value'])} | "
                     f"{pct(h['t']['green'], 1)} | {DOT[h['light']]} {WORD[h['light']]} |")
        else:
            L.append(f"| {label} | {count(n.get(key))} | | | | |")
    L.append("")
    L.append("Creative (video only):")
    L.append("")
    for c in r["creative"]:
        note = ""
        if c["key"] == "hook_rate" and n.get("_hooked_metric"):
            note = f" (from {n['_hooked_metric']})"
        L.append(f"- {c['t']['label']}{note}: {pct(c['value'])} {DOT[c['light']]} {WORD[c['light']]}")
    L.append("")

    L.append("## Fix next")
    L.append("")
    L.append(fix_next(r))
    L.append("")

    if r["ads"]:
        target_cost = camp.get("target_cost_per_result")
        total_spend = r["spend"] or 0
        L.append("## Every ad")
        L.append("")
        L.append(f"Target cost per {labels[early_key].lower()}: {money(target_cost, cur) if target_cost else 'not set yet'}. "
                 f"An ad is judged after {RULES['min_impressions_to_judge_ad']:,} impressions.")
        L.append("")
        L.append(f"| Ad | Spend | Share | Impr. | Link CTR | Hook | {labels[early_key]} | Cost each | Hint |")
        L.append("|---|---:|---:|---:|---:|---:|---:|---:|---|")
        ctr_t = goal["handoffs"]["ctr"]
        hook_t = TARGETS["creative"]["hook_rate"]
        for ad in sorted(r["ads"], key=lambda a: -(num(a.get("spend")) or 0)):
            spend = num(ad.get("spend")) or 0
            imp = num(ad.get("impressions"))
            ctr = ratio(num(ad.get("clicks")), imp)
            hook = ratio(num(ad.get("hooked")), imp)
            res = num(ad.get(early_key))
            ctr_l = light(ctr, ctr_t, imp)
            hook_l = light(hook, hook_t, imp)
            L.append(f"| {ad.get('name')} | {money(spend, cur)} | {pct(ratio(spend, total_spend), 0)} | {count(imp)} | "
                     f"{pct(ctr)} {DOT[ctr_l]} | {pct(hook)} {DOT[hook_l] if hook is not None else ''} | {count(res)} | "
                     f"{money(ratio(spend, res), cur)} | {ad_hint(ad, target_cost, early_key, cur)} |")
        L.append("")

    if r["placements"]:
        L.append("## Every placement")
        L.append("")
        L.append(f"| Placement | Spend | Impr. | Clicks | Link CTR | {labels[early_key]} | Cost each |")
        L.append("|---|---:|---:|---:|---:|---:|---:|")
        for p in sorted(r["placements"], key=lambda p: -(num(p.get("spend")) or 0)):
            spend, imp, clk = num(p.get("spend")), num(p.get("impressions")), num(p.get("clicks"))
            res = num(p.get(early_key))
            L.append(f"| {p.get('platform')} · {p.get('position')} | {money(spend, cur)} | {count(imp)} | {count(clk)} | "
                     f"{pct(ratio(clk, imp))} | {count(res)} | {money(ratio(spend, res), cur)} |")
        L.append("")

    base = camp.get("baseline")
    if base:
        bfolder = folder.parent / base
        if (bfolder / "campaign.json").exists():
            b = score_round(bfolder)
            L.append(f"## Against the baseline ({base})")
            L.append("")
            L.append("| What | Baseline | This round |")
            L.append("|---|---:|---:|")
            L.append(f"| Cost per {labels[score_key].lower()} | {money(b['cost_score'], cur)} | {money(r['cost_score'], cur)} |")
            L.append(f"| Cost per {labels[early_key].lower()} | {money(b['cost_early'], cur)} | {money(r['cost_early'], cur)} |")
            ft = camp.get("fix_target")
            if ft:
                bh = next((h for h in b["handoffs"] if h["key"] == ft), None)
                th = next((h for h in r["handoffs"] if h["key"] == ft), None)
                if bh and th:
                    L.append(f"| {th['t']['label']} (what we tried to fix) | {pct(bh['value'])} | {pct(th['value'])} {DOT[th['light']]} |")
                    L.append("")
                    L.append(suggest_verdict(r, bh, th))
            L.append("")

    (folder / "results.md").write_text("\n".join(L).rstrip() + "\n")
    return "\n".join(L)


def suggest_verdict(r, bh, th):
    if any(h[2] == "red" for h in r["health"]):
        return "**Suggested verdict:** none. A health light is red, so this isn't a fair test."
    d = r["days_since_change"]
    if d is not None and d < RULES["wait_days_after_change"]:
        return f"**Suggested verdict:** wait until day {RULES['wait_days_after_change']}."
    if th["light"] == "early" or bh["value"] is None or th["value"] is None:
        return "**Suggested verdict:** too early, not enough people on the step yet."
    better = th["value"] > bh["value"] if th["t"]["better"] == "higher" else th["value"] < bh["value"]
    return f"**Suggested verdict:** {'keep' if better else 'drop'} (judged only on the step we tried to fix). Badi makes the call."


# ---------------------------------------------------------------- scoreboard

def rebuild_scoreboard(companies_dir):
    rows, totals = [], {}
    for camp_file in sorted(companies_dir.glob("*/campaigns/*/campaign.json")):
        folder = camp_file.parent
        if folder.name.startswith("_") or folder.parent.parent.name.startswith("_"):
            continue
        r = score_round(folder)
        c = r["camp"]
        company = c.get("company") or folder.parent.parent.name
        labels = dict(r["goal"]["steps"])
        t = totals.setdefault(company, {"rounds": 0, "spend": 0, "score": 0, "label": labels[r["goal"]["score"]], "cur": r["cur"]})
        t["rounds"] += 1
        t["spend"] += r["spend"] or 0
        t["score"] += r["score_n"] or 0
        rows.append((company, c.get("name"), c.get("changed"), r))
    L = ["# Scoreboard", "",
         f"Rebuilt {dt.date.today().isoformat()} by scripts/ladder.py. Don't edit by hand.", "",
         "## The score per company", "",
         "| Company | Rounds | Spend | Score | Count | Cost each |",
         "|---|---:|---:|---|---:|---:|"]
    for company, t in totals.items():
        L.append(f"| {company} | {t['rounds']} | {money(t['spend'], t['cur'])} | {t['label']} | **{t['score']:.0f}** | "
                 f"{money(ratio(t['spend'], t['score']), t['cur'])} |")
    L += ["", "## Every round", "",
          "| Company | Round | What changed | Spend | Early signal | Cost each | Score | Cost each | Verdict |",
          "|---|---|---|---:|---:|---:|---:|---:|---|"]
    for company, name, changed, r in rows:
        L.append(f"| {company} | {name} | {changed} | {money(r['spend'], r['cur'])} | {count(r['early_n'])} | "
                 f"{money(r['cost_early'], r['cur'])} | {count(r['score_n'])} | {money(r['cost_score'], r['cur'])} | "
                 f"{r['camp'].get('verdict', 'pending')} |")
    (companies_dir / "SCOREBOARD.md").write_text("\n".join(L) + "\n")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", nargs="?", help="round folder (companies/<company>/campaigns/<round>)")
    ap.add_argument("--scoreboard", metavar="COMPANIES_DIR", help="rebuild SCOREBOARD.md for this folder")
    args = ap.parse_args()
    if args.scoreboard:
        print(rebuild_scoreboard(Path(args.scoreboard)))
        return
    if not args.folder:
        ap.error("give a round folder or --scoreboard companies")
    folder = Path(args.folder)
    r = score_round(folder)
    print(write_results(folder, r))
    companies_dir = folder.parent.parent.parent
    if companies_dir.name in ("companies", "examples"):
        rebuild_scoreboard(companies_dir)


if __name__ == "__main__":
    main()
