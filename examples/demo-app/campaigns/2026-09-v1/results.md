# Results: demo-app · 2026-09-v1

Scored 2026-10-13 by scripts/ladder.py. Don't edit by hand; rerun the script.
Numbers pulled from Meta: 2026-09-15T09:00. Goal: **App: paying subscribers**. Targets version 2026-10-13.

## The score

| What | Count | Cost each |
|---|---:|---:|
| **Paying subscriber** (the score) | **5** | **$112.00** |
| Installed (early signal) | 140 | $4.00 |
| Spend | $560.00 | |

## Health lights (stop if red)

| Light | Now | Green | Red | |
|---|---:|---:|---:|---|
| Frequency (times each person saw the ads) | 1.90x | 2.00x | 3.00x | 🟢 good |
| Rejected or limited ads | 0 | 0 | 1 | 🟢 good |
| Learning limited | no | no | yes | 🟢 good |
| Share of clicks from Audience Network | 52.0% | 20.0% | 50.0% | 🔴 fix |

## The ladder

| Step | People | Handoff | Rate | Green at | |
|---|---:|---|---:|---:|---|
| Seen | 30,000 | | | | |
| Clicked | 1,500 | Seen to clicked (link CTR) | 5.0% | 1.5% | 🟢 good |
| Installed | 140 | Clicked to installed | 9.3% | 25.0% | 🔴 fix |
| Started trial | 18 | Installed to started trial | 12.9% | 10.0% | 🟢 good |
| Paying subscriber | 5 | Trial to paying subscriber | 27.8% | 40.0% | 🟡 average |

Creative (video only):

- Hook rate (video): stopped scrolling (from 3-second video plays): 28.1% 🟡 average
- Hold rate (video): kept watching: 32.2% 🟡 average

## Fix next

**Setup first:** Share of clicks from Audience Network. Blended numbers are lying. Judge Facebook and Instagram placements apart, and ask Badi before excluding Audience Network. Don't judge creatives until this is green.

## Every ad

Target cost per installed: $6.00. An ad is judged after 1,000 impressions.

| Ad | Spend | Share | Impr. | Link CTR | Hook | Installed | Cost each | Hint |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A · Video · Control | $380.00 | 68% | 21,000 | 5.2% 🟢 | 28.1% 🟡 | 105 | $3.62 | winner candidate |
| B · Static · Challenger | $180.00 | 32% | 9,000 | 4.4% 🟢 | —  | 35 | $5.14 | winner candidate |

## Every placement

| Placement | Spend | Impr. | Clicks | Link CTR | Installed | Cost each |
|---|---:|---:|---:|---:|---:|---:|
| instagram · feed | $300.00 | 14,000 | 420 | 3.0% | 60 | $5.00 |
| facebook · feed | $200.00 | 9,000 | 300 | 3.3% | 45 | $4.44 |
| audience_network · an_classic | $60.00 | 7,000 | 780 | 11.1% | 35 | $1.71 |
