Score this round: $ARGUMENTS

1. Read campaign.json for the ad account and Meta campaign ID. Check the account matches company.md.
2. Pull from the Meta connector (fields in CLAUDE.md): per ad, and per placement
   (`publisher_platform` + `platform_position`). Do any read-only follow-ups the connector asks for.
3. Write pulled.json in the shape LOOP.md shows. Say in `hooked_metric` which video metric you used.
4. Make sure the down-funnel numbers in campaign.json → manual are current (ask Badi if not).
5. Run `python3 scripts/ladder.py <round folder>`.
6. Tell Badi in 3-5 short lines: is it still too early, any red health light, the biggest leak,
   the cost per score (and per early signal), and the one change you'd propose.
7. If the 7-day wait is over and he agrees with a verdict, write it in campaign.json and run /lesson.
8. Commit with a message like "<company> <round>: scored".
