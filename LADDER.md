# The ladder

Every person who sees an ad walks down these steps. Every round gets scored on all of them, so
we can see exactly where people drop off. The biggest drop is what we fix next.

**Each round has one goal, picked before launch.** The score is the real end of that goal.
The cheap step before it (installs, conversations, leads) is only the **early signal**: Meta
optimizes for it, so it can look great while the real end is empty.

The numbers live in [`targets.json`](targets.json). The script reads them from there.
This page explains them.

## The goals

| Goal | Steps | Early signal | **Score** |
|---|---|---|---|
| `app_subscriptions` | Seen → Clicked → Installed → Started trial → Paid | Installs | **Paying subscribers** |
| `whatsapp_sales` | Seen → Clicked → Conversation → Qualified → Sale | Conversations | **Sales** |
| `leads_booked` | Seen → Clicked → Lead → Booked → Won | Leads | **Clients won** |
| `ecommerce_sales` | Seen → Clicked → Added to cart → Purchase | Adds to cart | **Purchases** |

Where each number comes from:

| Number | Where |
|---|---|
| Seen, clicked, installs, conversations, leads, spend | Meta Ads connector, written to `pulled.json` |
| Trials, paid subs | App Store Connect / Firebase, typed into `campaign.json` → `manual` |
| Qualified, sales | The company's WhatsApp inbox, typed in by hand |
| Booked, won | Calendar or CRM, typed in by hand |

## Health lights (stop if red)

If any of these is red, the setup is the problem, not the creative. Fix it before judging.

| Light | Green | Red | Where the line comes from |
|---|---|---|---|
| Frequency | 2.0x or less | 3.0x or more | Cropink: cold audiences under 2 per week. Databox 2026: 3.01 median, all campaign types. |
| Rejected or limited ads | 0 | 1 or more | Our rule. |
| Learning limited | no | yes | Meta: about 50 optimization events per ad set in 7 days to leave learning. |
| Share of clicks from Audience Network | 20% or less | 50% or more | Our rule after L-002: on Peaches day 1, Audience Network gave 76% of clicks for 3% of spend. |

## Handoffs (step to step)

| Goal | Handoff | Red below | Green at or above | Judged after | Where the line comes from |
|---|---|---|---|---|---|
| all | Seen → clicked (link CTR) | 0.9% | 1.5% | 1,000 impressions | Databox 2026 (2,800+ companies): median link CTR 1.18%. **Over 8% is almost never real people.** |
| app | Clicked → installed | 10% | 25% | 100 clicks | AppTweak H1 2024 via Adapty: about 25% of US App Store page views install (all traffic). Paid social converts lower. |
| app | Installed → trial | 5% | 10% | 50 installs | Adapty: 7.3% download to trial in North America, 9.8% for higher-priced apps. |
| app | Trial → paid | 25% | 40% | 10 trials | RevenueCat 2026 (115,000+ apps): trials under 4 days 25.5% median, 17–32 days 42.5%. |
| WhatsApp | Clicked → conversation | 30% | 60% | 100 clicks | Our starting rule. Kanal 2026: no independent public benchmark exists. |
| WhatsApp | Conversation → qualified | 20% | 40% | 20 chats | Our starting rule. |
| WhatsApp | Qualified → sale | 15% | 30% | 10 people | Our starting rule. |
| leads | Clicked → lead | 4% | 8% | 100 clicks | WordStream (726 lead campaigns, 2024–25): 7.72% average. |
| leads | Lead → booked | 15% | 30% | 20 leads | Our starting rule. |
| leads | Booked → won | 15% | 30% | 10 people | Our starting rule. |
| store | Clicked → added to cart | 4% | 8% | 100 clicks | Our starting rule. |
| store | Added to cart → purchase | 25% | 40% | 20 carts | Our starting rule. Triple Whale 2025 (~35,000 stores): 1.6% median visit to purchase. |

Yellow means in between: normal, but not good yet.

## Creative (video ads)

| Number | Formula | Red below | Green at or above | Where the line comes from |
|---|---|---|---|---|
| Hook rate | 3-second plays ÷ impressions | 20% | 30% | AdSights via Superscale 2026: cold feed median about 22–23%, Reels about 30%. |
| Hold rate | ThruPlays ÷ 3-second plays | 25% | 40% | AdManage 2026 roundup of practitioner guides. Unverified. |

The connector didn't return 3-second plays on 2026-10-13. When it can't, hook rate shows
"no data" (or use 2-second continuous plays and say so in `pulled.json` → `hooked_metric`).

## Per ad

- An ad is judged after **1,000 impressions**.
- **Kill candidate:** spent 2x the target cost per early signal with nothing to show.
- **Winner candidate:** at or under the target cost, with 1,000+ impressions.
- Meta pushes money to what it likes. An ad with little spend is untested, not a loser.

## When a number is allowed to count

- **7 days after any change** (new ads, budget, audience). Meta needs about a week and ~50 events
  to learn; before that, numbers swing.
- The minimum people per step in the "Judged after" column.
- Trials need the trial length plus a few days before trial → paid can be read.

## These are starting lines, not forever lines

Most public benchmarks come from tool vendors or practitioners, and several lines above are our
own guess. Once a company has **3 judged rounds**, its own best round becomes the bar to beat.
If we change a line in `targets.json`, we write why in `playbook/lessons.md`.

## Sources (checked October 13, 2026)

- [Superscale · Meta ads benchmarks by industry (Databox, AdSights, Cropink, WordStream)](https://superscale.ai/learn/meta-ads-benchmarks-by-industry/)
- [AdManage · What is a good hook rate](https://admanage.ai/blog/what-is-a-good-hook-rate-for-facebook-ads)
- [RevenueCat · Subscription app trends and benchmarks 2026](https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026)
- [Adapty · App Store conversion rate](https://adapty.io/blog/app-store-conversion-rate/)
- [Adapty · Trial conversion rates for in-app subscriptions](https://adapty.io/blog/trial-conversion-rates-for-in-app-subscriptions/)
- [FindClout · Cost per install by channel 2026](https://findclout.com/blog/cost-per-install-by-channel-2026) (Meta iOS US planning range $3–6, unsourced)
- [Kanal · Click-to-WhatsApp ads benchmarks 2026](https://getkanal.com/blog/click-to-whatsapp-ads-benchmarks-2026)
- [Jetfuel · Meta ads learning phase 2026](https://jetfuel.agency/what-is-the-meta-ads-learning-phase-how-to-exit-it-faster-in-2026/)
