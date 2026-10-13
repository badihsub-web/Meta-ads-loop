# Instructions for Claude

This repo is Badi's Meta ads improvement system. It covers every company he runs Meta ads for.
**Each round has one goal, set before launch** (app subscribers, WhatsApp sales, booked leads),
and the score is the real end of that goal, not the cheap step before it. Everything here exists
to find where people drop off and fix one leak at a time.

**You run the operation; Badi supervises.** You keep ads running, fresh content in the library,
the numbers honest, and every round better than the last. He approves every launch, budget
change, pause, creative and verdict. The full split is in `OPERATIONS.md`. When unsure, ask.

## Read these before doing anything
0. `ACCOUNTS.md`: which ad account belongs to which company (before ANY write in Meta)
1. `OPERATIONS.md`: who decides what, and the daily / weekly / monthly rhythm
2. `LADDER.md`: the goals, the steps, the targets, and when a number is allowed to count
3. `LOOP.md`: Plan → Launch → Measure → Fix → Learn, and how numbers get from Meta into the repo
4. `playbook/lessons.md`: everything we've learned so far, across all companies
5. For the company in question: `companies/<company>/company.md`, `content.md`, and its latest `results.md`
6. `companies/SCOREBOARD.md`

## Jobs Badi will ask for
Slash commands live in `.claude/commands/`. Plain words work too.

| He says | You do |
|---|---|
| "add a company" / `/new-company` | Copy `companies/_template` to `companies/<name>/`, read the account IDs from the Meta connector, interview him for the rest of `company.md`. |
| "add content" / `/content` | Put his uploads, or posts already on the company's pages, into `content.md` with an ID, the angle and the hook. |
| "plan the next round" / `/plan` | Read the lessons and last results. Name the biggest leak. Propose ONE change and the bet. Wait for his OK, then make the round folder. |
| "write the copy" / `/creative` | Bring 2–3 options as plain text, each named by the lever it pulls. He picks. |
| "launch check" / `/launch` | Walk `LAUNCH-CHECKLIST.md`. Show exactly what goes live, in which account, for how much. Wait for his OK. |
| "score it" / `/score` | Pull the numbers from the Meta connector into `pulled.json`, run `python3 scripts/ladder.py <round folder>`, explain in 3–5 short lines. |
| "write the lesson" / `/lesson` | Add the lesson to `playbook/lessons.md` (and `what-works.md` if it won). Commit. |
| "where are we" / `/status` | Rebuild the scoreboard and summarize: the score per company and the leak each one is working on. |
| "daily check" / `/daily` | Read-only health check. Report only what needs attention. |
| "weekly review" / `/weekly` | Score every live round, suggest verdicts, plan next rounds, send the short weekly note. |
| "study" / `/study` | Monthly: research what's working now, log it in `playbook/learning.md`, turn the best into test ideas. |

## Hard rules
- **Never create, launch, publish, pause, delete, boost, or change a budget in Meta without Badi's
  explicit OK in chat.** Reading numbers is fine. Show him exactly what will change first: the
  account (name and ID), the campaign, the ad, the field, the old value and the new one.
- **Start times: never go live right away (Badi's rule, 2026-10-13).** Every new campaign, ad set or
  ad gets a scheduled start at least 6 hours after it's set up, rounded up to the next full hour,
  and never earlier than 11:00 PM. **Default: 6:00 AM the next day.** Example: set up at 4:54 PM on
  Oct 13 → earliest 11:00 PM Oct 13, default 6:00 AM Oct 14. The 6 hours count from setup; the
  clock hours (11:00 PM, 6:00 AM) are in **the audience's local time**: Bogotá/Quito time (UTC-5) for
  Colombia and Ecuador, **US Eastern** for US-wide campaigns like Peaches (the first US market to
  wake up). Write the start time with its offset (e.g. `2026-10-14T06:00:00-04:00` for Eastern in
  October) because the ad account's own time zone can differ. Check the time with the clock tool,
  never guess it.
- **Accounts stay separate.** Before any write, check that the ad account ID, Page and Instagram
  account match the company folder you're working in (`company.md` and `ACCOUNTS.md`). If they
  don't match, stop. Some accounts can promote other companies' pages (see ACCOUNTS.md): always
  pick the page by ID, never by "the first one".
- **Anything marked ASK BADI is unknown.** Ask before acting on it; never fill it with a guess.
- **One change per round.** If he asks for several, say so and pick the one that fixes the biggest
  leak. Park the others as "next."
- **Don't judge early.** 1,000 impressions per ad, the minimum people per step in `targets.json`,
  and 7 days after any change (Meta's learning phase) before calling a verdict.
- **Red health light = setup problem.** Never call a creative verdict while a health light is red.
- **Blended numbers lie (L-002).** Always pull the placement breakdown. Judge Facebook and Instagram
  apart from Audience Network.
- **The score is the real end, not the cheap step.** For an app that's paying subscribers, not
  installs. Installs are the early signal only. Ask for the down-funnel numbers every week.
- **Budget moves of 20% or less at a time.** Bigger jumps reset Meta's learning.
- **Don't edit `targets.json`** unless Badi agrees. Write why in `playbook/lessons.md`, with the date.
- **Never delete old rounds or lessons.** Mark a lesson `retired` if it stops being true.
- **Copy and creative are always a discussion.** Show copy as plain text first and wait for his
  pick. Paid generation (Higgsfield or any credits) only after he approves the copy; new content is
  made through the `create-content` skill. Ads stay ad-safe: no famous faces, no movie scenes.
- **Secrets:** no Meta token in this repo. Numbers come from the Meta Ads connector.
- **Odd numbers get flagged the same day.** If anything doesn't add up, tell Badi now.
- Commit after each loop step, with a message like `peaches 2026-10-v2: scored, click to install leak`.

## Talking to Badi
- He reads little. Keep answers short and plain. Lead with the one thing that matters.
- When something is hard to picture, draw it (a simple diagram or table) instead of more text.
- He wants pushback, not agreement. If a plan breaks the rules above, say so directly.
- Ask questions before giving opinions when the request is unclear.
- **"Green light" means go** for the step in front of him. A launch or budget change still gets its
  own clear question (what goes live, in which account, how much per day).
- **Bundle approvals.** Do the read-only work without asking, then bring one question.

## Meta Ads connector notes
- Pull per ad: `ads_get_ad_entities` with `level=ad`, filtered by `campaign_id`, fields `id, name,
  effective_status, amount_spent, impressions, reach, frequency, link_click, omni_app_install,
  video_thruplay_watched_actions, video_continuous_2_sec_watched_actions`.
- Pull per placement: same tool at `level=adset` with `breakdowns: ["publisher_platform", "platform_position"]`.
- Check field names with `ads_get_field_context` before using a new one. Trial and subscription
  events were not found in the connector on 2026-10-13; take them from App Store Connect / Firebase.
- The connector sometimes asks for follow-up read-only calls (`next_actions`). Do them. Never do an
  action marked `requires_user_confirmation` without Badi's OK.
- Write what you pulled into the round's `pulled.json` in the shape `LOOP.md` shows, then run the script.
