# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_edit_array_input import NimbleEditArrayInput

class TestNimbleEditArrayInput(unittest.TestCase):
    """NimbleEditArrayInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleEditArrayInput:
        """Test NimbleEditArrayInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleEditArrayInput`
        """
        model = NimbleEditArrayInput()
        if include_optional:
            return NimbleEditArrayInput(
                name = 'NimbleArray'
            )
        else:
            return NimbleEditArrayInput(
                name = 'NimbleArray',
        )
        """

    def testNimbleEditArrayInput(self):
        """Test NimbleEditArrayInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
