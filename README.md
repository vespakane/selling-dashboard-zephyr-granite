# Selling dashboard

A single-page, pixel-measured recreation of a mobile selling dashboard. Open `index.html` in a browser.

The figures are not typed in; the page simulates a long-running low-ticket shop and nothing needs setting up. Everything is computed from a fixed seed and the clock, so it shows the same numbers for any given instant on any device, catches up on time away, and refreshes itself every 15 seconds while open.

What the simulation does:

- **Revenue** drifts month to month between about £30k and £75k, with good and bad weeks on top. Most items sell for £5 to £15 at .49/.99 price points; about one order in fourteen is dearer (£15 to £40) and one in a hundred is £40 to £150.
- **Orders** get individual timestamps on a daily curve (quiet overnight, evening peak, weekends a little busier). The buyer-paid badge is today's orders so far and resets at midnight. The year-to-date total and the orders count are the sum and number of sales since 1 January (over £100 the total is shown in whole pounds, rounded down); the account has traded since before this year.
- **Funds** are the sales from three days earlier, released over the last 24 hours, minus the final value fee (12.8% plus 30p an order) and ad fees (about 45% of orders come through promoted listings at a 4 to 10% ad rate). Postage is bought off eBay, so nothing is deducted for it.
- **Feedback (last 30 days)** comes from about 24% of buyers, two to fourteen days after the sale; roughly 1% of it is negative and 0.7% neutral.
- **Send offer to buyers** is the number of listings with interested buyers, 3 to 8 percent of active listings, drifting day to day and moving with the listing count.
- **Active listings** stay within a band of about 1,200 to 1,800, changing by one at random moments through the day. **Inactive** listings are 2 to 6 percent of active, plus anything a stock-out has taken offline. The tiles abbreviate thousands, so 1,209 shows as 1.2k+.
- **Shocks**: roughly every month or two there is a demand slump (sales down 25 to 55 percent for 3 to 10 days) or a surge (up 30 to 90 percent for 2 to 6 days), a stock-out (listings fall by 120 to 400 over a few days, sales fall with them, then both recover as stock is relisted) or a restock (a batch of 100 to 300 new listings that lifts sales and sells through over a few weeks), plus the odd dead day and rare viral spike. Supply shocks can push the listing count outside its usual band for a while.

Tapping **Buyer paid - send now** opens the Orders screen, measured from captures of the real one in the same way. It lists today's unposted orders, one card each, as many as the listings added to it allow. **Post now** is that count; **All** is every order of the last two years; **Awaiting Feedback to buyer** is the orders where no feedback has been exchanged yet. Each card is drawn from the order's own timestamp, so it reads the same every time: the buyer id, a quantity of 2 or 3 now and then, a colour where the listing has colour options, whether it was sold via Promoted Listings, and the dates (buyer paid today or late yesterday, post by the day after). The items themselves come from the **Actions** button, which opens a sheet to add listings with a photo, title, price, optional colours and how many of today's orders each one gets; only those orders are listed, so five listings set to five orders each show 25 cards even on a busier day. Listings are kept in the browser's local storage on the device.

The device's own status bar sits above the page as an opaque bar, so nothing scrolls under it. Added to an iPhone home screen it opens full-screen as "eBay" with the icon in `assets/apple-touch-icon.png`.

`tools/` holds the headless-Chrome render and measurement scripts used to line the layout up against reference captures (the captures themselves are not included), plus `fixture.js`, test data for the Orders screen (`index.html?view=orders&fixture=tools/fixture.js`).
