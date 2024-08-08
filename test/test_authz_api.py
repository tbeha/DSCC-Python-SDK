# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.api.authz_api import AuthzApi


class TestAuthzApi(unittest.TestCase):
    """AuthzApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthzApi()

    def tearDown(self) -> None:
        pass

    def test_get_access_controls(self) -> None:
        """Test case for get_access_controls

        Get User Accessible Resources
        """
        pass

    def test_get_resource_types(self) -> None:
        """Test case for get_resource_types

        Get resource types with read permissions
        """
        pass


if __name__ == '__main__':
    unittest.main()
