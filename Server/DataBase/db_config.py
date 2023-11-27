from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB setup
uri = "mongodb+srv://amish920w:WZZXSYAlA1hBboq3@clustercheckout.zplphbp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database("SmartCheckout")

# Create a global variable for the database
db = database
