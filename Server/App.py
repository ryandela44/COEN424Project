from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Controllers.Customer import *
from Controllers.Item import *
from Controllers.ScanningSession import *
from Controllers.ScannedItem import *
from Controllers.SuperMarket import *

# MongoDB setup
uri = "mongodb+srv://amish920w:WZZXSYAlA1hBboq3@clustercheckout.zplphbp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database("SmartCheckout")

# Create a global variable for the database that can be imported in controller modules
db = database

app = Flask(__name__)


# Item Endpoints
@app.route('/v2/Item', methods=['GET'])
def get_items_route():
    # Call your controller function here
    return jsonify(get_items())


@app.route('/v2/Item', methods=['POST'])
def add_item_route():
    item_data = request.json
    return jsonify(add_item(item_data)), 201


@app.route('/v2/Item/<string:itemID>', methods=['GET', 'PUT', 'DELETE'])
def item_operations(itemID):
    if request.method == 'GET':
        return jsonify(get_item_by_id(itemID))
    elif request.method == 'PUT':
        item_data = request.json
        return jsonify(update_item(itemID, item_data)), 200
    elif request.method == 'DELETE':
        return jsonify(delete_item(itemID)), 200


# Customer Routes
@app.route('/v2/Customer', methods=['GET'])
def list_customers_route():
    return jsonify(list_customers())


@app.route('/v2/Customer', methods=['POST'])
def add_customer_route():
    customer = request.json
    return jsonify(add_customer(customer)), 201


@app.route('/v2/Customer/<string:customerID>', methods=['GET', 'PUT', 'DELETE'])
def customer_route(customerID):
    if request.method == 'GET':
        return jsonify(get_customer_by_id(customerID))
    elif request.method == 'PUT':
        customer_data = request.json
        return jsonify(update_customer(customerID, customer_data)), 200
    elif request.method == 'DELETE':
        return jsonify(delete_customer(customerID)), 200


# Supermarket Endpoints
@app.route('/v2/Supermarket', methods=['GET'])
def get_supermarkets():
    return jsonify(list_supermarkets())


@app.route('/v2/Supermarket', methods=['POST'])
def add_supermarket_route():
    supermarket_data = request.json
    return jsonify(add_supermarket(supermarket_data)), 201


@app.route('/v2/Supermarket/<string:supermarketID>', methods=['GET', 'PUT', 'DELETE'])
def supermarket_operations(supermarketID):
    if request.method == 'GET':
        return jsonify(get_supermarket_by_id(supermarketID))
    elif request.method == 'PUT':
        supermarket_data = request.json
        return jsonify(update_supermarket(supermarketID, supermarket_data)), 200
    elif request.method == 'DELETE':
        return jsonify(delete_supermarket(supermarketID)), 200


# Scanning Session Endpoints
@app.route('/v2/Customer/<string:customerID>/ScanningSession', methods=['GET'])
def list_sessions_route(customerID):
    return jsonify(list_sessions(customerID))


@app.route('/v2/Customer/<string:customerID>/ScanningSession', methods=['POST'])
def start_session_route(customerID):
    return jsonify(add_session(customerID)), 201


@app.route('/v2/Customer/<string:customerID>/ScanningSession/<string:sessionID>', methods=['GET', 'PUT', 'DELETE'])
def session_operations(customerID, sessionID):
    if request.method == 'GET':
        return jsonify(get_session_by_id(sessionID, customerID))
    elif request.method == 'PUT':
        session_data = request.json
        return jsonify(update_session(sessionID, customerID, session_data)), 200
    elif request.method == 'DELETE':
        return jsonify(delete_session(sessionID, customerID)), 200


# Scanned Item Endpoints
@app.route('/v2/Customer/<string:customerID>/ScanningSession/<string:sessionID>/ScannedItem', methods=['GET'])
def get_scanned_items_route(customerID, sessionID):
    return jsonify(list_scanned_items(sessionID, customerID))


@app.route('/v2/Customer/<string:customerID>/ScanningSession/<string:sessionID>/ScannedItem', methods=['POST'])
def add_scanned_item_route(customerID, sessionID):
    scanned_item_data = request.json
    return jsonify(add_scanned_item(sessionID, customerID, scanned_item_data)), 201


@app.route('/v2/Customer/<string:customerID>/ScanningSession/<string:sessionID>/ScannedItem/<string:scannedItemID>',
           methods=['GET', 'PUT', 'DELETE'])
def scanned_item_operations(customerID, sessionID, scannedItemID):
    if request.method == 'GET':
        return jsonify(get_scanned_item_by_id(scannedItemID, sessionID, customerID))
    elif request.method == 'PUT':
        scanned_item_data = request.json
        return jsonify(update_scanned_item(scannedItemID, sessionID, customerID, scanned_item_data)), 200
    elif request.method == 'DELETE':
        return jsonify(delete_scanned_item(scannedItemID, sessionID, customerID)), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
