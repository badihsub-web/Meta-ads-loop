Launch check for: $ARGUMENTS

1. Walk LAUNCH-CHECKLIST.md item by item. Check what you can with the Meta connector (account,
   Page, Instagram, payment, errors). Ask Badi about anything you can't check.
2. Walk section 2 of the round's campaign.md.
3. Show Badi one clear summary and wait for his explicit OK:
   account (name and ID) · campaign · goal and optimization event · audience · placements ·
   daily budget · every ad with its copy · the exact scheduled start time (date and hour).
4. Only after that OK, build it with the Meta connector, with a scheduled start time from the start-time
   rule in CLAUDE.md (at least 6 hours out, never before 11:00 PM, default 6:00 AM next day, Bogotá
   time with its offset). Read it back with `ads_get_ad_entities` and `ads_get_ad_preview`, show Badi
   the preview and the exact start time, then activate it with his go so it waits for that start time.
5. Record the Meta campaign ID, ad IDs, `first_live` and `last_change` in campaign.json and
   campaign.md. Commit.
6. Day-1 check: every ad delivering, none rejected, spend pacing. Tell Badi right away if not.
