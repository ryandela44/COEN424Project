# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.scanning_session import ScanningSession  # noqa: E501
from swagger_server.models.scanning_session_list import ScanningSessionList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestScanningSessionController(BaseTestCase):
    """ScanningSessionController integration test stubs"""

    def test_delete_session(self):
        """Test case for delete_session

        Delete By SessionID & CustomerID
        """
        response = self.client.open(
            '/v2/Customer/{CustomerID}/ScanningSession/{SessionID}'.format(session_id='38400000-8cf0-11bd-b23e-10b96e4ef00d', customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_session_by_id(self):
        """Test case for get_session_by_id

        Search By SessionID & CustomerID
        """
        response = self.client.open(
            '/v2/Customer/{CustomerID}/ScanningSession/{SessionID}'.format(session_id='38400000-8cf0-11bd-b23e-10b96e4ef00d', customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_sessions(self):
        """Test case for list_sessions

        List of All Active and Inactive Sessions Per Customer.
        """
        response = self.client.open(
            '/v2/Customer/{CustomerID}/ScanningSession'.format(customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_customer_customer_id_scanning_session_post(self):
        """Test case for v2_customer_customer_id_scanning_session_post

        Add a New Session for a Customer
        """
        body = [ScanningSession()]
        response = self.client.open(
            '/v2/Customer/{CustomerID}/ScanningSession'.format(customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v2_customer_customer_id_scanning_session_session_idput(self):
        """Test case for v2_customer_customer_id_scanning_session_session_idput

        Update By SessionID & CustomerID
        """
        body = ScanningSession()
        response = self.client.open(
            '/v2/Customer/{CustomerID}/ScanningSession/{SessionID}'.format(session_id='38400000-8cf0-11bd-b23e-10b96e4ef00d', customer_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
