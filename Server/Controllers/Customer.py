from Server.DataBase.db_config import db
from Server.Utility import serialize_doc
from bson import ObjectId


def list_customers():
    customers = list(db.Customer.find({}))
    return serialize_doc(customers)


def add_customer(customer_data):
    result = db.Customer.insert_one(customer_data)
    customer_data['_id'] = str(result.inserted_id)
    return serialize_doc(customer_data)


def get_customer_by_id(customerID):
    if not isinstance(customerID, ObjectId):
        customerID = ObjectId(customerID)
    customer = db.Customer.find_one({"CustomerID": customerID})
    return serialize_doc(customer)


def update_customer(customerID, customer_data):
    db.Customer.update_one({"CustomerID": customerID}, {"$set": customer_data})
    return serialize_doc(customer_data)


def delete_customer(customerID):
    db.Customer.delete_one({"CustomerID": customerID})
