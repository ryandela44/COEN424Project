import connexion
import six

from swagger_server.models.scanning_session import ScanningSession  # noqa: E501
from swagger_server.models.scanning_session_list import ScanningSessionList  # noqa: E501
from swagger_server import util


def delete_session(session_id, customer_id):  # noqa: E501
    """Delete By SessionID &amp; CustomerID

    Delete a Session by its Id value. # noqa: E501

    :param session_id: Session ID
    :type session_id: 
    :param customer_id: Customer ID
    :type customer_id: 

    :rtype: None
    """
    return 'do some magic!'


def get_session_by_id(session_id, customer_id):  # noqa: E501
    """Search By SessionID &amp; CustomerID

    Get a single **Scanning Session** by its Id value. # noqa: E501

    :param session_id: Session ID
    :type session_id: 
    :param customer_id: Customer ID
    :type customer_id: 

    :rtype: ScanningSession
    """
    return 'do some magic!'


def list_sessions(customer_id):  # noqa: E501
    """List of All Active and Inactive Sessions Per Customer.

    Get a list of sessions for that customer # noqa: E501

    :param customer_id: Customer ID
    :type customer_id: 

    :rtype: ScanningSessionList
    """
    return 'do some magic!'


def v2_customer_customer_id_scanning_session_post(customer_id, body=None):  # noqa: E501
    """Add a New Session for a Customer

    Scanned Items # noqa: E501

    :param customer_id: Customer ID
    :type customer_id: 
    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [ScanningSession.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def v2_customer_customer_id_scanning_session_session_idput(body, session_id, customer_id):  # noqa: E501
    """Update By SessionID &amp; CustomerID

    Update Scanning Session by id. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param session_id: Session ID
    :type session_id: 
    :param customer_id: Customer ID
    :type customer_id: 

    :rtype: None
    """
    if connexion.request.is_json:
        body = ScanningSession.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
