Run the daily check from OPERATIONS.md. Read only: never change anything in Meta here.

1. For every company with a live round: read its company.md for the ad account ID.
2. Meta connector: are the live ads delivering? Any rejected ads, account, payment or delivery errors (`ads_get_errors`)?
3. Spend today vs the daily budget: overspending, or stuck at zero?
4. Pull per ad and per placement for the live round, update pulled.json, run the script.
   Look at the health lights and the "kill candidate" hints.
5. Anything that looks odd (numbers that don't add up, a sudden jump) gets flagged to Badi today.
6. Report to Badi ONLY what needs attention, in 3 lines or fewer, each with the fix you'd propose.
   If everything is fine, say "All ads healthy" and stop. No creative verdicts from one day of data.
