from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["todoDB"]
collection = db["items"]

@app.route("/submittodoitem", methods=["POST"])
def submit_item():
    item_name = request.form.get("itemName")
    item_desc = request.form.get("itemDescription")

    if not item_name or not item_desc:
        return jsonify({"error": "Both fields required"}), 400

    # insert into MongoDB
    collection.insert_one({"name": item_name, "description": item_desc})
    
    return jsonify({"message": "Item added successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True)

