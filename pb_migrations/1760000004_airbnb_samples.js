migrate((db) => {
  const dao = new Dao(db);
  const c = dao.findCollectionByNameOrId("listings");
  // sample listings were entered as USD-style numbers: convert to KSh (x130)
  try { dao.db().newQuery("UPDATE listings SET price = price * 130, old_price = old_price * 130 WHERE type != 'airbnb'").execute(); } catch (e) { console.log("price conversion skipped", e); }
  const mk = (title, loc, price, size, bd, ba, desc, feat) => ({ title, type: "airbnb", status: "available", location: loc, price, size, bedrooms: bd, bathrooms: ba, description: desc, featured: feat, offer: false });
  [
    mk("Kilimani Skyline Studio", "Kilimani, Nairobi", 8500, 45, 1, 1, "Bright studio with city views, fast Wi-Fi, a fully equipped kitchenette and secure parking.", true),
    mk("Karen Garden Cottage", "Karen, Nairobi", 14000, 90, 2, 2, "Quiet cottage in a leafy compound with a private garden, fireplace and breakfast nook.", true),
    mk("Westlands Executive Apartment", "Westlands, Nairobi", 11500, 85, 2, 2, "Modern two-bedroom near restaurants and offices, with a gym, pool and 24/7 security.", false),
    mk("Runda Villa Retreat", "Runda, Nairobi", 38000, 320, 4, 4, "Spacious family villa with a pool, landscaped garden, staff quarters and ample parking.", true),
    mk("Muthaiga Heritage Suite", "Muthaiga, Nairobi", 22000, 120, 2, 2, "Elegant suite in a prestigious estate, with a private terrace and a dedicated workspace.", false),
    mk("Lavington Cosy Loft", "Lavington, Nairobi", 9500, 60, 1, 1, "Stylish loft with a king bed, a balcony and a calm, walkable neighbourhood.", false),
  ].forEach((r) => { try { const rec = new Record(c); Object.keys(r).forEach((k) => rec.set(k, r[k])); dao.saveRecord(rec); } catch (e) { console.log("seed skipped", e); } });
  return null;
}, (db) => {
  const dao = new Dao(db);
  try { dao.db().newQuery("DELETE FROM listings WHERE type = 'airbnb'").execute(); } catch (e) {}
  return null;
});
