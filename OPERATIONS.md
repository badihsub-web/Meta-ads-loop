# How we run it

We're a team. **Claude runs the operation. Badi supervises and approves.**
The goal: ads always running for every active company, fresh content always in the library,
the numbers always honest, and every round a little better than the last.

## Who decides what

| Decision | Claude | Badi |
|---|---|---|
| **The goal of a round** (subscribers, WhatsApp sales, booked leads) | Proposes it, with the score and the early signal | **Approves** before anything is built |
| **Ad copy and creative** | Brings 2–3 options as plain text, each with the lever it pulls | **Picks by feel.** The data shows later who was right. |
| **Paid generation** (Higgsfield or other credits) | Prepares it through `create-content` | **Approves the copy first.** Nothing spends before that. |
| **Launching, publishing or boosting** | Prepares everything, runs the launch check | **Says go.** Nothing goes live without his OK in chat. |
| **Budget changes, pausing, turning ads off** | Proposes with numbers (20% or less per move) | **Says go** |
| **Audience, placements, objective** | Proposes one change at a time, with the reason | **Approves** |
| **Keep or drop a round** | Scores it, suggests a verdict | **Makes the call** |
| **Changing a target in targets.json** | Proposes it with evidence | **Approves** |
| Pulling numbers, scoring, health lights | Does it | Gets the summary |
| Finding the leak, drafting the next test | Does it | Reviews the plan |
| Adding content to the library | Does it, tags angle and hook | Spot-checks |
| Writing lessons, updating the playbook | Does it | Reads the one-line summary |
| Studying what works out there | Does it, turns ideas into test proposals | Approves which ideas to test |

When unsure whether something needs approval: **ask.** Supervision is the point.

## The rhythm

### Every day (5 minutes, read only)
- [ ] Every live ad is delivering. No rejected ads, no account or payment problems.
- [ ] Spend is pacing with the budget (no overspend, no ads stuck at zero).
- [ ] Health lights: frequency, Audience Network share, learning limited.
- [ ] A clear loser burning money (spent 2x the target cost with nothing to show) → flag it.
- [ ] Anything odd → tell Badi the same day. Otherwise say "All ads healthy" and stop.

Daily is alarms only. **No creative verdicts from one day of data.**

### Every week
- [ ] Pull numbers for every live round (`/score`). Rebuild the scoreboard (`/status`).
- [ ] Ask Badi (or read the tool) for the down-funnel numbers: trials and paid subs, qualified
      WhatsApp chats and sales, booked calls. Type them into `campaign.json` → `manual`.
- [ ] Rounds past the 7-day wait with enough people → suggest the verdict, then `/lesson`.
- [ ] Next round planned for every company whose current test is judged (`/plan`).
- [ ] Content runway: each company has at least 2 untested pieces ready in `content.md`.
- [ ] Short weekly note to Badi: the score per company, the leak, what needs his approval.

### Every month
- [ ] Learning review: what's working on Meta now (`/study`). Best ideas → `playbook/test-ideas.md`.
- [ ] Look across companies: did a lesson from one work in another? Upgrade its confidence.
- [ ] Are the targets still right? Once a company has 3 judged rounds, its own best is the bar.
- [ ] Tools: is anything slowing us down? Recommend fixes to Badi (only tools that work with Claude).

## Content pipeline

Each company keeps its content in `companies/<company>/content.md`. A piece goes
**new → testing → winner / retired**. Sources, in order: Badi's uploads, posts already on the
company's pages, new pieces made with `create-content`.

## Tools we run on

| Job | Tool | Status |
|---|---|---|
| Reading numbers, creating and editing ads | Meta Ads connector (official) | Connected |
| Making new creative | `create-content` skill (Higgsfield, ElevenLabs) | Connected |
| App installs, trials, paid subs | App Store Connect / Firebase (Peaches) | Typed in by hand for now |
| WhatsApp conversations and sales | The company's WhatsApp inbox | Typed in by hand for now |
| Posting organic to Instagram / Facebook | Not set up | Next step: find a posting tool that works with Claude |
| Scoring and history | This repo + `scripts/ladder.py` | Ready |
| Running the rhythm on a schedule | Claude scheduled tasks | Not set up yet; needs Badi's OK |
