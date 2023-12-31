from Server.DataBase.db_config import db
from Server.Utility import serialize_doc
from bson import ObjectId


def list_scanned_items(sessionID, customerID):
    scanned_items = list(db.ScannedItems.find({"SessionID": sessionID, "CustomerID": customerID}))
    return serialize_doc(scanned_items)


def add_scanned_item(sessionID, customerID, scanned_item_data):
    scanned_item_data.update({"SessionID": sessionID, "CustomerID": customerID})

    # Check if the item already exists
    existing_item = db.ScannedItems.find_one({
        "ItemID": scanned_item_data['ItemID'],
        "SessionID": sessionID,
        "CustomerID": customerID
    })

    if existing_item:
        # Ensure Quantity is an integer before incrementing
        current_quantity = int(existing_item.get('Quantity', '0'))
        new_quantity = current_quantity + 1
        db.ScannedItems.update_one({"_id": existing_item['_id']}, {"$set": {"Quantity": new_quantity}})
        return serialize_doc(existing_item)
    else:
        # Insert a new item
        db.ScannedItems.insert_one(scanned_item_data)
        return serialize_doc(scanned_item_data)



def get_scanned_item_by_id(scannedItemID, sessionID, customerID):
    scanned_items = db.ScannedItems.find_one(
        {"ScannedItemID": scannedItemID, "SessionID": sessionID, "CustomerID": customerID})
    return serialize_doc(scanned_items)


def update_scanned_item(scannedItemID, sessionID, customerID, scanned_item_data):
    db.ScannedItems.update_one({"ScannedItemID": scannedItemID, "SessionID": sessionID, "CustomerID": customerID},
                              {"$set": scanned_item_data})
    return serialize_doc(scanned_item_data)


def delete_scanned_item(scannedItemID, sessionID, customerID):
    db.ScannedItems.delete_one({"ScannedItemID": scannedItemID, "SessionID": sessionID, "CustomerID": customerID})
