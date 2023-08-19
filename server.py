from flask import Flask, request, jsonify
import pymongo
from flask_cors import CORS
from bson import json_util

app = Flask(__name__)
CORS(app)

client = pymongo.MongoClient("mongodb+srv://devw:devw123456@cluster0.vp7tf8d.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("recipe-database")
recipe_collection = pymongo.collection.Collection(db, "recipes")

def add_recipe(name, ingredients, method):
    recipe = {"name": name, "ingredients": ingredients, "method": method}
    return recipe_collection.insert_one(recipe)

@app.route('/addrecipe', methods=['POST'])
def api_post_recipe():
    try:
        add_recipe(request.json.get('name'), request.json.get('ingredients'), request.json.get('method'))
        return jsonify({'Success': "Yay"})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/listrecipes', methods=['GET'])
def api_get_recipe():
    try:
        recipe_data = recipe_collection.find()
        return json_util.dumps(recipe_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/deleterecipe', methods=['POST'])
def api_post_deleterecipe():
    try:
        recipe_collection.delete_one(request.json)
        return jsonify({'Success': "Yay"})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=8000)