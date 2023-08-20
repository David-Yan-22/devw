import clientPromise from "../../lib/mongodb";

export default async function handler(req, res) {
  const client = await clientPromise;
  const db = await client.db("notes_db");
  console.log(req.body);
  const result = await db.collection("notes_col").deleteOne({"name": req.body});
  console.log(result);
  res.json({status: 200});
}
