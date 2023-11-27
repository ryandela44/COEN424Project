from Server.DataBase.db_config import db
from Server.Utility import serialize_doc
from bson import ObjectId


def list_scanned_items(sessionID, customerID):
    scanned_items = list(db.ScannedItems.find({"SessionID": sessionID, "CustomerID": customerID}))
    return serialize_doc(scanned_items)


def add_scanned_item(sessionID, customerID, scanned_item_data):
    scanned_item_data.update({"SessionID": sessionID, "CustomerID": customerID})
    result = db.ScannedItems.insert_one(scanned_item_data)
    scanned_item_data['_id'] = str(result.inserted_id)
    return serialize_doc(scanned_item_data)


def get_scanned_item_by_id(scannedItemID, sessionID, customerID):
    if not isinstance(scannedItemID, ObjectId):
        scannedItemID = ObjectId(scannedItemID)
    if not isinstance(sessionID, ObjectId):
        sessionID = ObjectId(sessionID)
    if not isinstance(customerID, ObjectId):
        customerID = ObjectId(customerID)
    scanned_items = db.ScannedItems.find_one(
        {"ScannedItemID": scannedItemID, "SessionID": sessionID, "CustomerID": customerID})
    return serialize_doc(scanned_items)


def update_scanned_item(scannedItemID, sessionID, customerID, scanned_item_data):
    db.ScannedItems.update_one({"ScannedItemID": scannedItemID, "SessionID": sessionID, "CustomerID": customerID},
                              {"$set": scanned_item_data})
    return serialize_doc(scanned_item_data)


def delete_scanned_item(scannedItemID, sessionID, customerID):
    db.ScannedItems.delete_one({"ScannedItemID": scannedItemID, "SessionID": sessionID, "CustomerID": customerID})
