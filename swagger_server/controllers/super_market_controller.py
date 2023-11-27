import connexion
import six

from swagger_server.models.super_market_list import SuperMarketList  # noqa: E501
from swagger_server.models.supermarket import Supermarket  # noqa: E501
from swagger_server import util


def delete_supermarket(supermarket_id):  # noqa: E501
    """Delete Super Market By ID

    Delete a Super Market by its Id value. # noqa: E501

    :param supermarket_id: Super Market ID
    :type supermarket_id: 

    :rtype: None
    """
    return 'do some magic!'


def get_supermarket_by_id(supermarket_id):  # noqa: E501
    """Search for Super Market By ID

    Get a single **Super Market** by its Id value. # noqa: E501

    :param supermarket_id: Super Market ID
    :type supermarket_id: 

    :rtype: Supermarket
    """
    return 'do some magic!'


def list_supermarket():  # noqa: E501
    """List of All Super Markets

    Get a list of Super Market in the system # noqa: E501


    :rtype: SuperMarketList
    """
    return 'do some magic!'


def v2_supermarket_post(body):  # noqa: E501
    """Add a New Super Market

    Create a new Super Market # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Supermarket.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v2_supermarket_supermarket_idput(body, supermarket_id):  # noqa: E501
    """Update Super Market by ID

    Update Super Market by id. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param supermarket_id: Super Market Id
    :type supermarket_id: 

    :rtype: None
    """
    if connexion.request.is_json:
        body = Supermarket.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
