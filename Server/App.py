import connexion
import uvicorn
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB setup
uri = "mongodb+srv://amish920w:WZZXSYAlA1hBboq3@clustercheckout.zplphbp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database("SmartCheckout")

# Create a global variable for the database that can be imported in controller modules
db = database

# Create the Connexion application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('COEN424_Raptors-SmartCheckout-v2.0-resolved.json')

if __name__ == '__main__':
    uvicorn.run("App:app", host="127.0.0.1", port=5000, log_level="debug", reload=True)