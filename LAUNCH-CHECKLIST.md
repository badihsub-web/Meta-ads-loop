# Launch checklist (step 0)

Run this before every launch. If anything fails, fix it before going live. A broken setup makes
every number below it meaningless.

## The right account
- [ ] Ad account name and ID match `company.md` and `ACCOUNTS.md` for this company
- [ ] The Page and Instagram account match `company.md` (picked by ID, not by name)
- [ ] Account is active, payment method works, no spending limit about to hit
- [ ] Currency is right (USD vs COP) and the budget is written in that currency

## Tracking
- [ ] The goal's events reach Meta: app installs (SDK), WhatsApp conversations, or leads
- [ ] We know where the down-funnel numbers come from (App Store Connect, Firebase, WhatsApp inbox)
      and who types them in each week
- [ ] App: the App Store link opens the right app in the right country

## Setup
- [ ] Objective and optimization event match the round's goal
- [ ] Enough budget to reach about 50 optimization events a week, or Badi knows it will run
      "learning limited" (budget ÷ target cost per event × 7)
- [ ] Placements decided on purpose (L-002: Audience Network can flood the click numbers)
- [ ] Audience written in `campaign.md` (location, age, language, device)
- [ ] No other live campaign in the same account fighting for the same people

## Creative
- [ ] Every ad's content is in `content.md` with an ID
- [ ] Copy below is exactly what's in Meta, approved by Badi as plain text
- [ ] Ad-safe: no famous faces, no movie scenes, no claims we can't back up
- [ ] The ad and the landing (store page, WhatsApp greeting) say the same thing
- [ ] Sizes fit the placements (9:16 for Reels and Stories, 4:5 or 1:1 for feed)

## Go
- [ ] Badi said go, after seeing: account, what goes live, daily budget, start date
- [ ] `campaign.json` has the Meta campaign ID, `first_live` and `last_change`
- [ ] **Day-1 check:** every ad is delivering, none rejected, spend is pacing
