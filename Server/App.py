from flask import Flask, request, jsonify
from Controllers.Customer import *
from Controllers.Item import *
from Controllers.ScanningSession import *
from Controllers.ScannedItem import *
from Controllers.SuperMarket import *
from Server.AIService.CustomVision import get_prediction_from_custom_vision
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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


@app.route('/V2/CustomVision/scan-item', methods=['POST'])
def scan_item():
    image_url = None
    image_file = None

    # Check the content type of the incoming request
    if request.content_type == 'application/json':
        # Handle JSON data
        customerID = request.json.get('customerID')
        sessionID = request.json.get('sessionID')
        image_url = request.json.get('image_url')
    elif 'multipart/form-data' in request.content_type:
        # Handle multipart/form-data (form data)
        customerID = request.form.get('customerID')
        sessionID = request.form.get('sessionID')
        image_file = request.files.get('image_file')
    else:
        return jsonify({"error": "Unsupported Media Type"}), 415

    if not sessionID:
        # If no sessionID is provided, create a new scanning session
        session_data = {"CustomerID": customerID}  # Add any necessary session data
        session = add_session(customerID, session_data)
        sessionID = session['_id']

    # Call the prediction function
    prediction = get_prediction_from_custom_vision(image_url=image_url, image_file=image_file)
    if not prediction or 'predictions' not in prediction:
        return jsonify({"error": "Failed to get prediction"}), 500

    # Process the prediction and add scanned items to the session
    for pred in prediction['predictions']:
        if pred['probability'] > 0.70:  # Threshold for probability
            item_name = pred['tagName']
            item = get_item_by_name(item_name)
            if item:
                scanned_item_data = {
                    "ItemID": item['ItemID'],
                    "Price": item['UnitPrice'],
                    "Quantity": 1  # Set initial quantity
                }
                add_scanned_item(sessionID, customerID, scanned_item_data)

    # Calculate the total price for the session
    scanned_items = list_scanned_items(sessionID, customerID)
    total_price = sum(int(item.get('Price', 0)) * int(item.get('Quantity', 1)) for item in scanned_items)

    response = {
        "session_id": sessionID,
        "scanned_items": scanned_items,
        "total_price": total_price
    }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
