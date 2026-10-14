# Selling dashboard

A single-page, pixel-measured recreation of a mobile selling dashboard. Open `index.html` in a browser.

The figures are not typed in; the page simulates a long-running low-ticket shop and nothing needs setting up. Everything is computed from a fixed seed and the clock, so it shows the same numbers for any given instant on any device, catches up on time away, and refreshes itself every 15 seconds while open.

What the simulation does:

- **Revenue** drifts month to month between about £30k and £75k, with good and bad weeks on top. Most items sell for £5 to £15 at .49/.99 price points; about one order in fourteen is dearer (£15 to £40) and one in a hundred is £40 to £150.
- **Orders** get individual timestamps on a daily curve (quiet overnight, evening peak, weekends a little busier). The buyer-paid badge is today's orders so far and resets at midnight. The year-to-date total and the orders count are the sum and number of sales since 1 January; the account has traded since before this year.
- **Funds** are the sales from three days earlier, released over the last 24 hours, minus the final value fee (12.8% plus 30p an order) and ad fees (about 45% of orders come through promoted listings at a 4 to 10% ad rate). Postage is bought off eBay, so nothing is deducted for it.
- **Feedback (last 30 days)** comes from about 24% of buyers, two to fourteen days after the sale; roughly 1% of it is negative and 0.7% neutral.
- **Send offer to buyers** is the number of listings with interested buyers, 3 to 8 percent of active listings, drifting day to day and moving with the listing count.
- **Active listings** stay within a band of about 1,200 to 1,800, changing by one at random moments through the day.
- **Shocks**: roughly every month or two there is a demand slump (sales down 25 to 55 percent for 3 to 10 days) or a surge (up 30 to 90 percent for 2 to 6 days), a stock-out (listings fall by 120 to 400 over a few days, sales fall with them, then both recover as stock is relisted) or a restock (a batch of 100 to 300 new listings that lifts sales and sells through over a few weeks), plus the odd dead day and rare viral spike. Supply shocks can push the listing count outside its usual band for a while.

The device's own status bar sits above the page; the page leaves room for it on notched phones. Added to an iPhone home screen it opens full-screen as "eBay" with the icon in `assets/apple-touch-icon.png`.

`tools/` holds the headless-Chrome render and measurement scripts used to line the layout up against reference captures (the captures themselves are not included).
