from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Retrieve MongoDB URI from environment variables
mongodb_uri = os.getenv("MONGODB_URI")

# MongoDB setup 
client = MongoClient(mongodb_uri server_api=ServerApi('1'))
database = client.get_database("SmartCheckout")

# Create a global variable for the database
db = database

