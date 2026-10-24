# Round: peaches · 2026-10-trial-v2

First round on the new offer (7-day free trial, $39.99/year, $7.99/month; Badi confirmed live 2026-10-24).
The offer changed, so v1 isn't a fair comparison. This is a new baseline built from week 1's lessons.
Plan approved by Badi 2026-10-24.

## 1 · Plan

- **Goal:** app_subscriptions · **score:** paid subs
- **Max cost per paying subscriber:** $35 (Claude's rec, Badi asked "what do you rec?"; break even on one year plan, about $34 after Apple)
- **Target cost per early signal:** $7 per install as a holding bar (v1 real-feed cost was $7.71). Reality check: at $7 per install we need 1 in 5 installs to pay to hit $35. Week 1 tells us if that's possible.
- **Audience:** US · 25–40 · iPhone · English (check Advantage+ audience isn't widening it to 18+, L-007)
- **Placements:** Facebook + Instagram only (no Audience Network)
- **Daily budget:** $25 USD → about 3 installs a day at ~$7.70, far under Meta's ~50 a week. Learning stays limited; accepted for now.
- **Start:** Sun 2026-10-25 06:00 Eastern (`2026-10-25T06:00:00-04:00`), runs to at least Nov 1 (7 days, L-007)
- **Baseline:** this is the baseline for the trial offer
- **The ONE thing we changed:** placements (FB+IG only). Also fixed, not tested: 3 ads instead of 7 (L-006), copy in English with the real offer (L-008), sorting game gets money (L-009)
- **Leak we're fixing:** Audience Network 76% of clicks (red health light in v1)
- **Bet:** If all spend goes to Facebook + Instagram, real-people installs go from 14 a week to ~20 a week, and we see the first trials and paid subs.
- **Lessons we read first:** L-001, L-002, L-006, L-007, L-008, L-009

## 2 · Launch check

- [ ] LAUNCH-CHECKLIST.md passed
- [ ] Copy below is exactly what's in Meta
- [ ] campaign.json has the Meta IDs, `first_live` and `last_change`
- [ ] Badi said go

## 3 · Ads (exactly as live)

| Ad | Content ID | Format | Primary text | Headline | Control or challenger |
|---|---|---|---|---|---|
| 01 · Static · 23 things | C-001 | Static | (copy pending /creative) | | baseline |
| 02 · Carousel · You're not lazy | C-002 | Carousel | (copy pending /creative) | | baseline |
| 03 · Video · Sorting game | C-003 | Video | (copy pending /creative) | | baseline |

## 4 · Results

Pull `pulled.json` from the Meta connector, type trials and paid subs into `campaign.json`,
then run `python3 scripts/ladder.py <this folder>`. Don't judge before 7 days after the last change.

## 5 · Fix and lesson

- **What happened:** 
- **Verdict:** 
- **Lesson (one sentence):** 
- **Applies to:** 
- **Next round will change:** 
