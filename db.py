from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://devw:devw123456@cluster0.vp7tf8d.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)

db = client.get_database("flask_mongodb_recipes")

# collecddtion JSON
collection = pymongo.collection.Collection(db, "collection")