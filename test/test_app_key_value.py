# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.app_key_value import AppKeyValue

class TestAppKeyValue(unittest.TestCase):
    """AppKeyValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppKeyValue:
        """Test AppKeyValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppKeyValue`
        """
        model = AppKeyValue()
        if include_optional:
            return AppKeyValue(
                key = 'key1',
                value = 'value1'
            )
        else:
            return AppKeyValue(
        )
        """

    def testAppKeyValue(self):
        """Test AppKeyValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
