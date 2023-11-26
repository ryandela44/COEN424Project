from Server.DataBase.db_config import db
from Server.Utility import serialize_doc
from bson import ObjectId


def list_scanned_items(sessionID, customerID):
    scanned_items = list(db.ScannedItem.find({"SessionID": sessionID, "CustomerID": customerID}))
    return serialize_doc(scanned_items)


def add_scanned_item(sessionID, customerID, scanned_item_data):
    scanned_item_data.update({"SessionID": sessionID, "CustomerID": customerID})
    result = db.ScannedItem.insert_one(scanned_item_data)
    scanned_item_data['_id'] = str(result.inserted_id)
    return serialize_doc(scanned_item_data)


def get_scanned_item_by_id(scannedItemID, sessionID, customerID):
    if not isinstance(scannedItemID, ObjectId):
        scannedItemID = ObjectId(scannedItemID)
    if not isinstance(sessionID, ObjectId):
        sessionID = ObjectId(sessionID)
    if not isinstance(customerID, ObjectId):
        customerID = ObjectId(customerID)
    scanned_item = db.ScannedItem.find_one(
        {"ScannedItemID": scannedItemID, "SessionID": sessionID, "CustomerID": customerID})
    return serialize_doc(scanned_item)


def update_scanned_item(scannedItemID, sessionID, customerID, scanned_item_data):
    db.ScannedItem.update_one({"ScannedItemID": scannedItemID, "SessionID": sessionID, "CustomerID": customerID},
                              {"$set": scanned_item_data})
    return serialize_doc(scanned_item_data)


def delete_scanned_item(scannedItemID, sessionID, customerID):
    db.ScannedItem.delete_one({"ScannedItemID": scannedItemID, "SessionID": sessionID, "CustomerID": customerID})
