import connexion
import six

from swagger_server.models.item import Item  # noqa: E501
from swagger_server.models.item_list import ItemList  # noqa: E501
from swagger_server import util


def delete_item(item_id):  # noqa: E501
    """Delete an Item by ID

     # noqa: E501

    :param item_id: Item ID
    :type item_id: 

    :rtype: None
    """
    return 'do some magic!'


def get_item_by_id(item_id):  # noqa: E501
    """Search for an Item by ID

     # noqa: E501

    :param item_id: Item ID
    :type item_id: 

    :rtype: Item
    """
    return 'do some magic!'


def v2_item_get():  # noqa: E501
    """List of All Items

     # noqa: E501


    :rtype: ItemList
    """
    return 'do some magic!'


def v2_item_item_idput(body, item_id):  # noqa: E501
    """Update an Item by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param item_id: Item Id
    :type item_id: 

    :rtype: None
    """
    if connexion.request.is_json:
        body = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v2_item_post(body):  # noqa: E501
    """Add a New Item

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
