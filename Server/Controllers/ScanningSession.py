from Server.Controllers.Customer import get_customer_by_id
from Server.DataBase.db_config import db
from Server.Utility import serialize_doc


def list_sessions(customerID):
    sessions = list(db.ScanningSession.find({"CustomerID": customerID}))
    return serialize_doc(sessions)


def add_session(customerID, session_data):
    if get_customer_by_id(customerID):
        session_data.update({"CustomerID": customerID})
        db.ScanningSession.insert_one(session_data)
    return serialize_doc(session_data)


def get_session_by_id(sessionID, customerID):
    session = db.ScanningSession.find_one({"SessionID": sessionID, "CustomerID": customerID})
    return serialize_doc(session)


def update_session(sessionID, customerID, session_data):
    db.ScanningSession.update_one({"SessionID": sessionID, "CustomerID": customerID}, {"$set": session_data})
    return serialize_doc(session_data)


def delete_session(sessionID, customerID):
    db.ScanningSession.delete_one({"SessionID": sessionID, "CustomerID": customerID})
