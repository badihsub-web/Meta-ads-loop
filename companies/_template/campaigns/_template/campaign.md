# Round: <company> · <name>

One file per round. Fill it top to bottom as the loop moves. Never delete old rounds:
they are how we get better.

## 1 · Plan

- **Goal:** <app_subscriptions | whatsapp_sales | leads_booked> · **score:** <paid subs | sales | clients won>
- **Target cost per early signal:** <e.g. $5 per install>
- **Audience:** <place, age, language, device>
- **Placements:** <automatic, or which ones and why>
- **Daily budget:** <amount and currency> → about <n> optimization events a week
- **Baseline:** <which round we compare against, or "this is the baseline">
- **The ONE thing we changed:** <angle | hook | format | audience | placements | offer | landing | budget>
- **Leak we're fixing:** <the red step from the last results.md>
- **Bet:** If we <change>, then <step> goes from <before %> to <goal %>.
- **Lessons we read first:** <IDs from playbook/lessons.md>

## 2 · Launch check

- [ ] LAUNCH-CHECKLIST.md passed
- [ ] Copy below is exactly what's in Meta
- [ ] campaign.json has the Meta IDs, `first_live` and `last_change`
- [ ] Badi said go

## 3 · Ads (exactly as live)

| Ad | Content ID | Format | Primary text | Headline | Control or challenger |
|---|---|---|---|---|---|
| | | | | | |

## 4 · Results

Pull `pulled.json` from the Meta connector, type the down-funnel numbers into `campaign.json`,
then run `python3 scripts/ladder.py <this folder>`. It writes results.md next to this file.
Don't judge before 7 days after the last change.

## 5 · Fix and lesson

- **What happened:** 
- **Verdict:** keep | drop
- **Lesson (one sentence):** 
- **Applies to:** this company only | all companies
- **Next round will change:** 
