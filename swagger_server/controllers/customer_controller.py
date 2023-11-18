import connexion
import six

from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server.models.customer_list import CustomerList  # noqa: E501
from swagger_server import util


def delete_customer_v1(customer_id):  # noqa: E501
    """Delete Customer By ID

    Delete a customer by its Id value. # noqa: E501

    :param customer_id: Customer Id
    :type customer_id: 

    :rtype: None
    """
    return 'do some magic!'


def get_customer_by_id(customer_id):  # noqa: E501
    """Search for Customer By ID

    Get a single **Customer** by its Id value. # noqa: E501

    :param customer_id: Customer ID
    :type customer_id: 

    :rtype: Customer
    """
    return 'do some magic!'


def list_customers():  # noqa: E501
    """List of All Customers

    Get a list of customers in the system # noqa: E501


    :rtype: CustomerList
    """
    return 'do some magic!'


def v2_customer_customer_idput(body, customer_id):  # noqa: E501
    """Update Customer by ID

    Update customer by id. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param customer_id: Customer Id
    :type customer_id: 

    :rtype: None
    """
    if connexion.request.is_json:
        body = Customer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v2_customer_post(body):  # noqa: E501
    """Add a New Customer

    Create a new customer # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Customer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
