# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.super_market_list import SuperMarketList  # noqa: E501
from swagger_server.models.supermarket import Supermarket  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSuperMarketController(BaseTestCase):
    """SuperMarketController integration test stubs"""

    def test_delete_supermarket(self):
        """Test case for delete_supermarket

        Delete Super Market By ID
        """
        response = self.client.open(
            '/v2/Supermarket/{SupermarketID}'.format(supermarket_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_supermarket_by_id(self):
        """Test case for get_supermarket_by_id

        Search for Super Market By ID
        """
        response = self.client.open(
            '/v2/Supermarket/{SupermarketID}'.format(supermarket_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_supermarket(self):
        """Test case for list_supermarket

        List of All Super Markets
        """
        response = self.client.open(
            '/v2/Supermarket',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_supermarket_post(self):
        """Test case for v2_supermarket_post

        Add a New Super Market
        """
        body = Supermarket()
        response = self.client.open(
            '/v2/Supermarket',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_supermarket_supermarket_idput(self):
        """Test case for v2_supermarket_supermarket_idput

        Update Super Market by ID
        """
        body = Supermarket()
        response = self.client.open(
            '/v2/Supermarket/{SupermarketID}'.format(supermarket_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
