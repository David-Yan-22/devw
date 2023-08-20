// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

import clientPromise from "../../lib/mongodb.js"

export default async function handler(req, res){

  const client = await clientPromise;
  const db = await client.db("notes_db");
  switch (req.method){
    case "POST":
      console.log(req.body);
      await db.collection("notes_col").insertOne(req.body);
      res.json({status: 200});
      break;
    case "GET":
      const notes = await db.collection("notes_col").find({}).toArray();
      res.json(notes);
      break;
  }
}