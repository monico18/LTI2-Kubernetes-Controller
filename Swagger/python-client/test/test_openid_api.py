# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.29.4+k3s1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.openid_api import OpenidApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOpenidApi(unittest.TestCase):
    """OpenidApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.openid_api.OpenidApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_service_account_issuer_open_id_keyset(self):
        """Test case for get_service_account_issuer_open_id_keyset

        """
        pass


if __name__ == '__main__':
    unittest.main()
