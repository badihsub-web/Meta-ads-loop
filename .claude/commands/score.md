Score this round: $ARGUMENTS

1. Read campaign.json for the ad account and Meta campaign ID. Check the account matches company.md.
2. Pull from the Meta connector (fields in CLAUDE.md): per ad, and per placement
   (`publisher_platform` + `platform_position`). Do any read-only follow-ups the connector asks for.
3. Write pulled.json in the shape LOOP.md shows. Say in `hooked_metric` which video metric you used.
4. Make sure the down-funnel numbers in campaign.json → manual are current (ask Badi if not).
5. Run `python3 scripts/ladder.py <round folder>`.
6. Look at every ad's content next to its numbers: the hook (first line, first frame), the angle,
   the format, and whether the copy matches what people get after the click. Write what you see in
   content.md (best result, and a note per angle).
7. Tell Badi the feedback block in 3-5 short lines: Working / Not working / Try next, with the
   numbers, plus any red health light and whether it's still too early to judge.
8. If the 7-day wait is over and he agrees with a verdict, write it in campaign.json and run /lesson.
9. Commit with a message like "<company> <round>: scored".
