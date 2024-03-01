# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.rpc_status import RpcStatus  # noqa: E501
from swagger_server.models.v1_user import V1User  # noqa: E501
from swagger_server.models.v1_users import V1Users  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserServiceController(BaseTestCase):
    """UserServiceController integration test stubs"""

    def test_user_service_create_user(self):
        """Test case for user_service_create_user

        
        """
        query_string = [('name', 'name_example'),
                        ('age', 789)]
        response = self.client.open(
            '/users',
            method='POST',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_service_delete_user(self):
        """Test case for user_service_delete_user

        
        """
        response = self.client.open(
            '/users/{id}'.format(id='id_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_service_delete_users(self):
        """Test case for user_service_delete_users

        
        """
        response = self.client.open(
            '/users',
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_service_get_users(self):
        """Test case for user_service_get_users

        
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/users',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
