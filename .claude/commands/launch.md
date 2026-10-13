Launch check for: $ARGUMENTS

1. Walk LAUNCH-CHECKLIST.md item by item. Check what you can with the Meta connector (account,
   Page, Instagram, payment, errors). Ask Badi about anything you can't check.
2. Walk section 2 of the round's campaign.md.
3. Show Badi one clear summary and wait for his explicit OK:
   account (name and ID) · campaign · goal and optimization event · audience · placements ·
   daily budget · every ad with its copy · start date.
4. Only after that OK, build it with the Meta connector. Create it paused first, read it back with
   `ads_get_ad_entities` and `ads_get_ad_preview`, show Badi the preview, then turn it on with his go.
5. Record the Meta campaign ID, ad IDs, `first_live` and `last_change` in campaign.json and
   campaign.md. Commit.
6. Day-1 check: every ad delivering, none rejected, spend pacing. Tell Badi right away if not.
