import connexion
import six

from swagger_server.models.scanned_item import ScannedItem  # noqa: E501
from swagger_server.models.scanned_item_list import ScannedItemList  # noqa: E501
from swagger_server import util


def delete_scanned_item(scanned_item_id, session_id, customer_id):  # noqa: E501
    """Delete a Scanned Item by ID

     # noqa: E501

    :param scanned_item_id: Scanned Item ID
    :type scanned_item_id: 
    :param session_id: Session ID
    :type session_id: 
    :param customer_id: Customer ID
    :type customer_id: 

    :rtype: None
    """
    return 'do some magic!'


def get_scanned_item_by_id(scanned_item_id, session_id, customer_id):  # noqa: E501
    """Search for a Scanned Item by ID

     # noqa: E501

    :param scanned_item_id: Scanned Item ID
    :type scanned_item_id: 
    :param session_id: Session ID
    :type session_id: 
    :param customer_id: Customer ID
    :type customer_id: 

    :rtype: ScannedItem
    """
    return 'do some magic!'


def v2_customer_customer_id_scanning_session_session_id_scanned_item_get(session_id, customer_id):  # noqa: E501
    """List of All the Scanned Items

     # noqa: E501

    :param session_id: Session ID
    :type session_id: 
    :param customer_id: Customer ID
    :type customer_id: 

    :rtype: ScannedItemList
    """
    return 'do some magic!'


def v2_customer_customer_id_scanning_session_session_id_scanned_item_post(body, session_id, customer_id):  # noqa: E501
    """Add a New Scanned Item

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param session_id: Session ID
    :type session_id: 
    :param customer_id: Customer ID
    :type customer_id: 

    :rtype: None
    """
    if connexion.request.is_json:
        body = ScannedItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v2_customer_customer_id_scanning_session_session_id_scanned_item_scanned_item_idput(body, scanned_item_id, session_id, customer_id):  # noqa: E501
    """Update a Scanned Item by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param scanned_item_id: Scanned Item Id
    :type scanned_item_id: 
    :param session_id: Session ID
    :type session_id: 
    :param customer_id: Customer ID
    :type customer_id: 

    :rtype: None
    """
    if connexion.request.is_json:
        body = ScannedItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
