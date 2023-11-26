from flask import Flask, request, jsonify
from Controllers.Customer import *
from Controllers.Item import *
from Controllers.ScanningSession import *
from Controllers.ScannedItem import *
from Controllers.SuperMarket import *

app = Flask(__name__)


# Item Routes
@app.route('/v2/Item', methods=['GET'])
def get_items_route():
    return jsonify(get_items()), 200


@app.route('/v2/Item', methods=['POST'])
def add_item_route():
    return jsonify(add_item(request.json)), 201


@app.route('/v2/Item/<string:itemID>', methods=['GET', 'PUT', 'DELETE'])
def item_operations(itemID):
    if request.method == 'GET':
        return jsonify(get_item_by_id(itemID)), 200
    elif request.method == 'PUT':
        return jsonify(update_item(itemID, request.json)), 204
    elif request.method == 'DELETE':
        delete_item(itemID)
        return jsonify({'message': 'Item Deleted'}), 200


# Customer Routes
@app.route('/v2/Customer', methods=['GET'])
def list_customers_route():
    return jsonify(list_customers()), 200


@app.route('/v2/Customer', methods=['POST'])
def add_customer_route():
    return jsonify(add_customer(request.json)), 201


@app.route('/v2/Customer/<string:customerID>', methods=['GET', 'PUT', 'DELETE'])
def customer_operations(customerID):
    if request.method == 'GET':
        return jsonify(get_customer_by_id(customerID)), 200
    elif request.method == 'PUT':
        return jsonify(update_customer(customerID, request.json)), 204
    elif request.method == 'DELETE':
        delete_customer(customerID)
        return jsonify({'message': 'Customer Deleted'}), 200


# Supermarket Routes
@app.route('/v2/Supermarket', methods=['GET'])
def get_supermarkets_route():
    return jsonify(list_supermarkets()), 200


@app.route('/v2/Supermarket', methods=['POST'])
def add_supermarket_route():
    print(request.json)
    return jsonify(add_supermarket(request.json)), 201


@app.route('/v2/Supermarket/<string:supermarketID>', methods=['GET', 'PUT', 'DELETE'])
def supermarket_operations(supermarketID):
    print(request.json)
    if request.method == 'GET':
        return jsonify(get_supermarket_by_id(supermarketID)), 200
    elif request.method == 'PUT':
        return jsonify(update_supermarket(supermarketID, request.json)), 204
    elif request.method == 'DELETE':
        delete_supermarket(supermarketID)
        return jsonify({'message': 'Supermarket Deleted'}), 200


# Scanning Session Routes
@app.route('/v2/Customer/<string:customerID>/ScanningSession', methods=['GET'])
def list_sessions_route(customerID):
    print(request.json)
    return jsonify(list_sessions(customerID)), 200


@app.route('/v2/Customer/<string:customerID>/ScanningSession', methods=['POST'])
def add_session_route(customerID):
    print(request.json)
    return jsonify(add_session(customerID, request.json)), 201


@app.route('/v2/Customer/<string:customerID>/ScanningSession/<string:sessionID>', methods=['GET', 'PUT', 'DELETE'])
def session_operations(customerID, sessionID):
    print(request.json)
    if request.method == 'GET':
        return jsonify(get_session_by_id(sessionID, customerID)), 200
    elif request.method == 'PUT':
        return jsonify(update_session(sessionID, customerID, request.json)), 204
    elif request.method == 'DELETE':
        delete_session(sessionID, customerID)
        return jsonify({'message': 'Session Deleted'}), 200


# Scanned Item Routes
@app.route('/v2/Customer/<string:customerID>/ScanningSession/<string:sessionID>/ScannedItem', methods=['GET'])
def get_scanned_items_route(customerID, sessionID):
    print(request.json)
    return jsonify(list_scanned_items(sessionID, customerID)), 200


@app.route('/v2/Customer/<string:customerID>/ScanningSession/<string:sessionID>/ScannedItem', methods=['POST'])
def add_scanned_item_route(customerID, sessionID):
    print(request.json)
    return jsonify(add_scanned_item(sessionID, customerID, request.json)), 201


@app.route('/v2/Customer/<string:customerID>/ScanningSession/<string:sessionID>/ScannedItem/<string:scannedItemID>',
           methods=['GET', 'PUT', 'DELETE'])
def scanned_item_operations(customerID, sessionID, scannedItemID):
    print(request.json)
    if request.method == 'GET':
        return jsonify(get_scanned_item_by_id(scannedItemID, sessionID, customerID)), 200
    elif request.method == 'PUT':
        return jsonify(update_scanned_item(scannedItemID, sessionID, customerID, request.json)), 204
    elif request.method == 'DELETE':
        delete_scanned_item(scannedItemID, sessionID, customerID)
        return jsonify({'message': 'Scanned Item Deleted'}), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
