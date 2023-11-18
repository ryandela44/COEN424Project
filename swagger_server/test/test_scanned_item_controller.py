# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.scanned_item import ScannedItem  # noqa: E501
from swagger_server.models.scanned_item_list import ScannedItemList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestScannedItemController(BaseTestCase):
    """ScannedItemController integration test stubs"""

    def test_delete_scanned_item(self):
        """Test case for delete_scanned_item

        Delete a Scanned Item by ID
        """
        response = self.client.open(
            '/v2/Customer/{CustomerID}/ScanningSession/{SessionID}/ScannedItem/{ScannedItemID}'.format(scanned_item_id='38400000-8cf0-11bd-b23e-10b96e4ef00d', session_id='38400000-8cf0-11bd-b23e-10b96e4ef00d', customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_scanned_item_by_id(self):
        """Test case for get_scanned_item_by_id

        Search for a Scanned Item by ID
        """
        response = self.client.open(
            '/v2/Customer/{CustomerID}/ScanningSession/{SessionID}/ScannedItem/{ScannedItemID}'.format(scanned_item_id='38400000-8cf0-11bd-b23e-10b96e4ef00d', session_id='38400000-8cf0-11bd-b23e-10b96e4ef00d', customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_customer_customer_id_scanning_session_session_id_scanned_item_get(self):
        """Test case for v2_customer_customer_id_scanning_session_session_id_scanned_item_get

        List of All the Scanned Items
        """
        response = self.client.open(
            '/v2/Customer/{CustomerID}/ScanningSession/{SessionID}/ScannedItem'.format(session_id='38400000-8cf0-11bd-b23e-10b96e4ef00d', customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_customer_customer_id_scanning_session_session_id_scanned_item_post(self):
        """Test case for v2_customer_customer_id_scanning_session_session_id_scanned_item_post

        Add a New Scanned Item
        """
        body = ScannedItem()
        response = self.client.open(
            '/v2/Customer/{CustomerID}/ScanningSession/{SessionID}/ScannedItem'.format(session_id='38400000-8cf0-11bd-b23e-10b96e4ef00d', customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_customer_customer_id_scanning_session_session_id_scanned_item_scanned_item_idput(self):
        """Test case for v2_customer_customer_id_scanning_session_session_id_scanned_item_scanned_item_idput

        Update a Scanned Item by ID
        """
        body = ScannedItem()
        response = self.client.open(
            '/v2/Customer/{CustomerID}/ScanningSession/{SessionID}/ScannedItem/{ScannedItemID}'.format(scanned_item_id='38400000-8cf0-11bd-b23e-10b96e4ef00d', session_id='38400000-8cf0-11bd-b23e-10b96e4ef00d', customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
