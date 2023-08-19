# link: https://dev.to/kouul/frmp-stack-5g9

from flask import Flask, redirect, url_for, jsonify, request
import pymongo
from flask_cors import CORS, cross_origin
import json
from datetime import datetime
from bson import json_util

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database called 'notes_db'
db = client.get_database("notes_db")

# Set up the collection of database fields (json objects)
notes_col = db.get_collection("notes_col")


# Add a new note
def add_notes(title, content, date):
    note = {"title": title, "content": content, "date": date}
    return notes_col.insert_one(note)

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
        note_data = notes_col.find()
        
        # convert db format from python dic to JSON format
        return json_util.dumps(note_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

# Edit note
@app.route('/editnote/<str:title>', methods=['POST', 'GET'])
def editnote(title):
    if request.method == 'GET':
        return ""
    
    if request.method == 'POST':
        return ""

if __name__ == "__main__":
    app.run(debug=True, port=8000)