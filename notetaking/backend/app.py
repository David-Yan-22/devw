# link: https://dev.to/kouul/frmp-stack-5g9

from flask import Flask, redirect, url_for, jsonify, request
import pymongo
from flask_cors import CORS, cross_origin
import json
from datetime import datetime
from bson import json_util

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'body-Type'


client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database called 'notes_db'
db = client.get_database("notes_db")

# Set up the collection of database fields (json objects)
notes_col = pymongo.collection.Collection(db, "notes_col")


# Add a new note
def add_notes(title,body):
    note = {"title": title, "body":body, "date": datetime.now()}
    return notes_col.insert_one(note)
'''
def try_add_note(id, title, content):
    note = {"_id": id, "title": title, "content": content, "date": datetime.now()}
    return notes_col.insert_one(note)

def get_note():
    try:
        note_data = notes_col.find()
        return json_util.dumps(note_data)
    except Exception as e:
        return jsonify({'error':str(e)}), 400

try_add_note(1, "Assignments", "Submit to lms")
'''

allList = []

def add_note(title, content):
    allList.append({"title" : title,
                    "body" : content})
    return

add_note("Assignments", "submit to lms")
add_note("To Do", "Get groceries, get new detergent")
add_note("Shopping", "Get groceries, get new detergent")
add_note("Deadlines", "Get groceries, get new detergent")
add_note("Bucket List", "Get groceries, get new detergent")
add_note("Travel", "Get groceries, get new detergent")
add_note("News", "Get groceries, get new detergent")
add_note("Plans", "Get groceries, get new detergent")
    

@app.route('/addnote', methods=['POST', 'GET'])
def api_post_note():
    if request.method == 'POST':
        try:
            add_notes(request.json.get('title'), request.json.get('body'))
            return jsonify({'Success': "Yay"})
        except Exception as e:
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
@app.route('/editNote/<int:id>', methods=['POST', 'GET'])
def editnote(id):
    if request.method == 'GET':
        selected_note = notes_col.find({'_id':id})
        for n in selected_note:
            request.form['title'] = n['title']
            request.form['body'] = n['body']
    
    if request.method == 'POST':
        notes_col.update_one(
            {'_id': id},
            {
                '$set':
                {
                    'title': request.form['title'],
                    'body': request.form['body'],
                    'date': datetime.now()
                }
            }
        )

        return redirect(url_for('home'))
    
    return "<h1>404 Not Found</h1>"

@app.route('/api/home', methods=['GET'])
def return_home():
    return jsonify(
        allList
    )


if __name__ == "__main__":
    app.run(debug=True, port=3000)