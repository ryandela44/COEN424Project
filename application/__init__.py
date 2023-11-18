from flask import Flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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

from application import routes