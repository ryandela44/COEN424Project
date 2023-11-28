from Server.DataBase.db_config import db
from Server.Utility import serialize_doc
from bson import ObjectId


def list_supermarkets():
    supermarkets = list(db.Supermarket.find({}))
    return serialize_doc(supermarkets)


def add_supermarket(supermarket_data):
    db.Supermarket.insert_one(supermarket_data)
    return serialize_doc(supermarket_data)


def get_supermarket_by_id(supermarketID):
    supermarket = db.Supermarket.find_one({"SupermarketID": supermarketID})
    return serialize_doc(supermarket)


def update_supermarket(supermarketID, supermarket_data):
    db.Supermarket.update_one({"SupermarketID": supermarketID}, {"$set": supermarket_data})
    return serialize_doc(supermarket_data)


def delete_supermarket(supermarketID):
    db.Supermarket.delete_one({"SupermarketID": supermarketID})
