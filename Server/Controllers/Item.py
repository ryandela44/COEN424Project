from Server.App import db
from Server.Utility import serialize_doc
from bson import ObjectId


def get_items():
    items = list(db.Item.find({}))
    return serialize_doc(items)


def add_item(item_data):
    result = db.Item.insert_one(item_data)
    item_data['_id'] = str(result.inserted_id)
    return serialize_doc(item_data)


def get_item_by_id(itemID):
    if not isinstance(itemID, ObjectId):
        itemID = ObjectId(itemID)
    item = db.Item.find_one({"ItemID": itemID})
    return serialize_doc(item)


def update_item(itemID, item_data):
    if not isinstance(itemID, ObjectId):
        itemID = ObjectId(itemID)

    db.Item.update_one({"_id": itemID}, {"$set": item_data})
    updated_item = db.Item.find_one({"_id": itemID})
    return serialize_doc(updated_item)


def delete_item(itemID):
    if not isinstance(itemID, ObjectId):
        itemID = ObjectId(itemID)
    db.Item.delete_one({"ItemID": itemID})
