# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.rekettye import Rekettye  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPlanetController(BaseTestCase):
    """PlanetController integration test stubs"""

    def test_alma_fun(self):
        """Test case for alma_fun

        Create a new planet
        """
        body = Rekettye()
        response = self.client.open(
            '/alma',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_post(self):
        """Test case for create_post

        Create a new planet
        """
        body = 'body_example'
        response = self.client.open(
            '/create',
            method='POST',
            data=json.dumps(body),
            content_type='text/plain')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
