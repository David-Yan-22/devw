from flask import Flask, request, jsonify
import pymongo
from flask_cors import CORS
from bson import json_util

app = Flask(__name__)
CORS(app)

client = pymongo.MongoClient("mongodb+srv://devw:devw123456@cluster0.vp7tf8d.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("note-database")
note_collection = pymongo.collection.Collection(db, "note")

def add_recipe(title, content, date):
    note = {"title": title, "content": content, "date": date}
    return note_collection.insert_one(note)

@app.route('/addnote', methods=['POST'])
def api_post_note():
    try:
        add_recipe(request.json.get('title'), request.json.get('content'), request.json.get('date'))
        return jsonify({'Success': "Yay"})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/listnotes', methods=['GET'])
def api_get_notes():
    try:
        note_data = note_collection.find()
        return json_util.dumps(note_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/editnote/<int:number>', methods=['GET'])
def editnote(number):
    return ""

if __name__ == "__main__":
    app.run(debug=True, port=8000)