# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_uninitialized_array_input import NimbleUninitializedArrayInput

class TestNimbleUninitializedArrayInput(unittest.TestCase):
    """NimbleUninitializedArrayInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleUninitializedArrayInput:
        """Test NimbleUninitializedArrayInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleUninitializedArrayInput`
        """
        model = NimbleUninitializedArrayInput()
        if include_optional:
            return NimbleUninitializedArrayInput(
                id = 'c463732d6436306437370000000000000000000000'
            )
        else:
            return NimbleUninitializedArrayInput(
                id = 'c463732d6436306437370000000000000000000000',
        )
        """

    def testNimbleUninitializedArrayInput(self):
        """Test NimbleUninitializedArrayInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
