migrate((db) => {
  const dao = new Dao(db);
  const c = dao.findCollectionByNameOrId("listings");
  c.schema.getFieldByName("type").options.values = ["sale", "rent", "land", "commercial", "airbnb"];
  if (!c.schema.getFieldByName("airbnb_url")) c.schema.addField(new SchemaField({ name: "airbnb_url", type: "url" }));
  return dao.saveCollection(c);
}, (db) => {
  const dao = new Dao(db);
  const c = dao.findCollectionByNameOrId("listings");
  c.schema.getFieldByName("type").options.values = ["sale", "rent", "land", "commercial"];
  c.schema.removeField(c.schema.getFieldByName("airbnb_url").id);
  return dao.saveCollection(c);
});
