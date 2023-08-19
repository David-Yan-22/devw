from flask import Flask, request, jsonify
import pymongo
from flask_cors import CORS
from bson import json_util

app = Flask(__name__)
CORS(app)

# Connect the MongoDB 
client = pymongo.MongoClient("mongodb+srv://devw:devw123456@cluster0.vp7tf8d.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("note-database")
note_collection = pymongo.collection.Collection(db, "note")


# Add a new note
def add_notes(title, content, date):
    note = {"title": title, "content": content, "date": date}
    return note_collection.insert_one(note)

@app.route('/addnote', methods=['POST'])
def api_post_note():
    try:
        add_notes(request.json.get('title'), request.json.get('content'), request.json.get('date'))
        return jsonify({'Success': "Yay"})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# index page, list all notes
@app.route('/listnotes', methods=['GET'])
def api_get_notes():
    try:
        note_data = note_collection.find()
        return json_util.dumps(note_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Edit note
@app.route('/editnote/<int:id>', methods=['POST', 'GET'])
def editnote(id):
    if request.method == 'GET':
        return ""
    
    if request.method == 'POST':
        return ""

if __name__ == "__main__":
    app.run(debug=True, port=8000)