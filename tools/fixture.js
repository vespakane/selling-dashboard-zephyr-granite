// Test data for the orders screen: ?view=orders&fixture=tools/fixture.js[&set=07]
// Mirrors the reference captures (screenshots/06.png and 07.png) so the render lines up with them.
window.FIXTURE = {
  today: '2026-10-14T13:38:00',
  counts: { all2y: '55', buyerPaid: '8', awaiting: '55' },
  listings: [
    { title: 'Oral-B Pro Precision Clean Toothbrush Heads | 8 Pack | New & Sealed', price: 9.25, img: 'tools/render/oralb8.jpg', colours: [], promoted: true, count: 5 },
    { title: 'Oral-B Pro Cross Action Electric Toothbrush Heads | 4 Pack | White or Black', price: 7.05, img: 'tools/render/oralb4.jpg', colours: ['White', 'Black'], promoted: true, count: 3 }
  ],
  // set=live leaves the orders to the simulation (the dealing code path)
  orders: /set=live/.test(location.search) ? null : /set=07/.test(location.search)
    ? [{ listing: 0, qty: 2, promoted: true, buyer: 'khybas-5' }, { listing: 1, qty: 1, colour: 'White', promoted: true, buyer: 'hedav6719' }]
    : [{ listing: 0, qty: 1, promoted: true, buyer: 'moyrwrigh_0' }, { listing: 0, qty: 2, promoted: true, buyer: 'khybas-5' }]
};
