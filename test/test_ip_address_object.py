# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.ip_address_object import IPAddressObject

class TestIPAddressObject(unittest.TestCase):
    """IPAddressObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IPAddressObject:
        """Test IPAddressObject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IPAddressObject`
        """
        model = IPAddressObject()
        if include_optional:
            return IPAddressObject(
                ip_addr = '10.0.0.11'
            )
        else:
            return IPAddressObject(
        )
        """

    def testIPAddressObject(self):
        """Test IPAddressObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
