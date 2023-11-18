from flask import Flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.collection import Collection
from pymongo.database import Database
from application import app
from flask import jsonify

app = Flask(__name__)
uri = "mongodb+srv://amish920w:WZZXSYAlA1hBboq3@clustercheckout.zplphbp.mongodb.net/?retryWrites=true&w=majority"


# set up mongoDB
#mongodb_client

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# add in your database and collection from Atlas 
database: Database = client.get_database("SmartCheckout")
collection: Collection = database.get_collection("Item")


# Something like this
# Endpoint to get item information by ProductName
@app.route('/Item/<string:ProductName>', methods=['GET'])
def get_item(ProductName):
    item = collection.find_one({"ProductName": ProductName})
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

