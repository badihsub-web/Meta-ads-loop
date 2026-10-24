# Round: peaches · 2026-10-trial-v2

First round on the new offer (7-day free trial, $39.99/year, $7.99/month; Badi confirmed live 2026-10-24).
The offer changed, so v1 isn't a fair comparison. This is a new baseline built from week 1's lessons.
Plan approved by Badi 2026-10-24.

## 1 · Plan

- **Goal:** app_subscriptions · **score:** paid subs
- **Max cost per paying subscriber:** $35 (Claude's rec, Badi asked "what do you rec?"; break even on one year plan, about $34 after Apple)
- **Target cost per early signal:** $7 per install as a holding bar (v1 real-feed cost was $7.71). Reality check: at $7 per install we need 1 in 5 installs to pay to hit $35. Week 1 tells us if that's possible.
- **Audience:** US · 25–40 · iPhone · English (check Advantage+ audience isn't widening it to 18+, L-007)
- **Structure (Badi, 2026-10-24):** 1 campaign · 3 ad sets, $20/day each (ad set budgets) · the same 5 ads in each
  - 01 Interest: US, 25–40, iPhone, productivity / planner / to-do app interests, Advantage+ audience off
  - 02 Demographic: US, 25–40, iPhone, no interests, Advantage+ audience off
  - 03 Retarget: engaged with the Peaches Page or Instagram, or watched our ads, last 60 days, minus people who installed. Badi chose $20/day; Claude recommended $8 (only ~2,000 people). Watch frequency daily; flag at 3x.
- **Placements:** Facebook + Instagram only (no Audience Network)
- **Daily budget:** $60 USD total → about 2–3 installs a day per ad set at ~$7.70, far under Meta's ~50 a week. Learning stays limited; accepted for now. ~$420 for 7 days (October has $482 left).
- **Start:** Sun 2026-10-25 06:00 Eastern (`2026-10-25T06:00:00-04:00`), runs to at least Nov 1 (7 days, L-007)
- **Baseline:** this is the baseline for the trial offer
- **The ONE thing we changed:** placements (FB+IG only). Also fixed, not tested: 5 best-performing pieces instead of 7 (L-006, L-009), copy in English with the real offer (L-008), sorting game gets money (L-009)
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
| 01 · Static · 23 things | C-001 | Static | Your list has 23 things. Only 3 actually matter. Peaches splits your day into Non-Negotiables and Flexible. Try it free for 7 days. | Do the 3 that matter | baseline (best ad v1: $4.30/install) |
| 02 · Carousel · You're not lazy | C-002 | Carousel | You're not lazy. Every task just looks urgent. Pick the 3 that can't move today and let the rest be Flexible. Try it free for 7 days. | Peaches: Your day, in two lists | baseline (2nd ad v1: $4.96/install) |
| 03 · Video · Quick game | C-003 | Video 39s | Quick game: Non-Negotiable or Flexible? Sort your day before your coffee's done. Try Peaches free for 7 days. | Sort your day | baseline (best organic: 433 views) |
| 04 · Video · Whole to-do list (Ferni UGC) | C-004 | Video 13.5s | Your whole to-do list isn't due today. List the few that can't move. Everything else can wait. Try Peaches free for 7 days. | Not everything is urgent | baseline (2nd organic: 190 views) |
| 05 · Video · Quick game round 2 | C-009 | Video 24s | Round two. One second each: Non-Negotiable or Flexible? Try Peaches free for 7 days. | Play the 5-second game | baseline (new, no numbers yet) |

## 4 · Results

Pull `pulled.json` from the Meta connector, type trials and paid subs into `campaign.json`,
then run `python3 scripts/ladder.py <this folder>`. Don't judge before 7 days after the last change.

## 5 · Fix and lesson

- **What happened:** 
- **Verdict:** 
- **Lesson (one sentence):** 
- **Applies to:** 
- **Next round will change:** 
