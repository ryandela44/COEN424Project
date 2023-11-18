# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.item import Item  # noqa: E501
from swagger_server.models.item_list import ItemList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestItemController(BaseTestCase):
    """ItemController integration test stubs"""

    def test_delete_item(self):
        """Test case for delete_item

        Delete an Item by ID
        """
        response = self.client.open(
            '/v2/Item/{ItemID}'.format(item_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_item_by_id(self):
        """Test case for get_item_by_id

        Search for an Item by ID
        """
        response = self.client.open(
            '/v2/Item/{ItemID}'.format(item_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_item_get(self):
        """Test case for v2_item_get

        List of All Items
        """
        response = self.client.open(
            '/v2/Item',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_item_item_idput(self):
        """Test case for v2_item_item_idput

        Update an Item by ID
        """
        body = Item()
        response = self.client.open(
            '/v2/Item/{ItemID}'.format(item_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_item_post(self):
        """Test case for v2_item_post

        Add a New Item
        """
        body = Item()
        response = self.client.open(
            '/v2/Item',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
