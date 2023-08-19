from flask import Flask, jsonify, request
from bson import ObjectId

from db import db

app = Flask(__name__)

@app.route("/")
def flask_mongodb_atlas():
    return "Hello world"

@app.route("/add_note")
def add_note():
    return "add note"

@app.route("/edit_note/<int:number>")
def edit_note(number):
    return "edit note"



"""Will sort out soon!"""

"""@app.route("/test")
def test():
    db.collection.insert_one({"name": "devw"})
    return "Connected to database"""

"""
@app.route("/get-all")
def get_all():
    all = db.collection.find()

    data = []
    for doc in all:
        doc["_id"] = str(doc["_id"])
        data.append(doc)
    return jsonify(data)"""


if __name__ == "__main__":
    app.run(port=8000, debug=True)