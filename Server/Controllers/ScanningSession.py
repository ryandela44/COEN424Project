from Server.DataBase.db_config import db
from Server.Utility import serialize_doc
from bson import ObjectId


def list_sessions(customerID):
    sessions = list(db.ScanningSession.find({"CustomerID": customerID}))
    return serialize_doc(sessions)


def add_session(customerID, session_data):
    session_data["CustomerID"] = customerID
    result = db.ScanningSession.insert_one(session_data)
    session_data['_id'] = str(result.inserted_id)
    return serialize_doc(session_data)


def get_session_by_id(sessionID, customerID):
    if not isinstance(sessionID, ObjectId):
        sessionID = ObjectId(sessionID)
    if not isinstance(customerID, ObjectId):
        customerID = ObjectId(customerID)
    session = db.ScanningSession.find_one({"SessionID": sessionID, "CustomerID": customerID})
    return serialize_doc(session)


def update_session(sessionID, customerID, session_data):
    if not isinstance(sessionID, ObjectId):
        sessionID = ObjectId(sessionID)
    if not isinstance(customerID, ObjectId):
        customerID = ObjectId(customerID)
    db.ScanningSession.update_one({"SessionID": sessionID, "CustomerID": customerID}, {"$set": session_data})
    return serialize_doc(session_data)


def delete_session(sessionID, customerID):
    if not isinstance(sessionID, ObjectId):
        sessionID = ObjectId(sessionID)
    if not isinstance(customerID, ObjectId):
        customerID = ObjectId(customerID)
    db.ScanningSession.delete_one({"SessionID": sessionID, "CustomerID": customerID})
