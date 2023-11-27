# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server.models.customer_list import CustomerList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCustomerController(BaseTestCase):
    """CustomerController integration test stubs"""

    def test_delete_customer_v1(self):
        """Test case for delete_customer_v1

        Delete Customer By ID
        """
        response = self.client.open(
            '/v2/Customer/{CustomerID}'.format(customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_customer_by_id(self):
        """Test case for get_customer_by_id

        Search for Customer By ID
        """
        response = self.client.open(
            '/v2/Customer/{CustomerID}'.format(customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_customers(self):
        """Test case for list_customers

        List of All Customers
        """
        response = self.client.open(
            '/v2/Customer',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_customer_customer_idput(self):
        """Test case for v2_customer_customer_idput

        Update Customer by ID
        """
        body = Customer()
        response = self.client.open(
            '/v2/Customer/{CustomerID}'.format(customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_customer_post(self):
        """Test case for v2_customer_post

        Add a New Customer
        """
        body = Customer()
        response = self.client.open(
            '/v2/Customer',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
