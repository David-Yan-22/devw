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

# Record the number of entities in DB (also use as id)
row_num = notes_col.find().count()


# Add a new note
def add_notes(title, content):
    global row_num
    row_num += 1
    note = {"_id": row_num, "title": title, "content": content, "date": datetime.now()}
    return notes_col.insert_one(note)

@app.route('/addnote', methods=['POST'])
def api_post_note():
    try:
        add_notes(request.json.get('title'), request.json.get('content'))
        return jsonify({'Success': "Yay"})
    except Exception as e:
        global row_num
        row_num -= 1
        return jsonify({'error': str(e)}), 400
    

# home page, list all notes
@app.route('/home', methods=['GET'])
def api_get_notes():
    try:
        note_data = notes_col.find()

        # convert db format from python dic to JSON format
        return json_util.dumps(note_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

# Edit note
@app.route('/editnote/<int:id>', methods=['POST', 'GET'])
def editnote(id):

    if request.method == 'GET':
        selected_note = notes_col.find({'_id':id})
        for n in selected_note:
            request.form['title'] = n['title']
            request.form['content'] = n['content']
    
    if request.method == 'POST':
        notes_col.update_one(
            {'_id': id},
            {
                '$set':
                {
                    'title': request.form['title'],
                    'content': request.form['content'],
                    'date': datetime.now()
                }
            }
        )

        return redirect(url_for('home'))
    
    return "<h1>404 Not Found</h1>"

@app.route('/api/home', methods=['GET'])
def return_home():
    return jsonify({
        'message' : 'David'
    })

if __name__ == "__main__":
    app.run(debug=True, port=3000)
