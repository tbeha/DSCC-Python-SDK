# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_health_status_without_sort_key import NimbleHealthStatusWithoutSortKey

class TestNimbleHealthStatusWithoutSortKey(unittest.TestCase):
    """NimbleHealthStatusWithoutSortKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleHealthStatusWithoutSortKey:
        """Test NimbleHealthStatusWithoutSortKey
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleHealthStatusWithoutSortKey`
        """
        model = NimbleHealthStatusWithoutSortKey()
        if include_optional:
            return NimbleHealthStatusWithoutSortKey(
                array_id = '1300000000000004d30000000000000001',
                context = 'all',
                ctrlr_id = '1300000000000004d30000000000000001',
                id = '1300000000000004d30000000000000001',
                scope = 'array'
            )
        else:
            return NimbleHealthStatusWithoutSortKey(
        )
        """

    def testNimbleHealthStatusWithoutSortKey(self):
        """Test NimbleHealthStatusWithoutSortKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
