# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_iscsi_initiator import NimbleISCSIInitiator

class TestNimbleISCSIInitiator(unittest.TestCase):
    """NimbleISCSIInitiator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleISCSIInitiator:
        """Test NimbleISCSIInitiator
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleISCSIInitiator`
        """
        model = NimbleISCSIInitiator()
        if include_optional:
            return NimbleISCSIInitiator(
                id = '021c9973433673c3db000000000000000000000001',
                ip_address = 'xx.xxx.xx.xx',
                iqn = 'vegaiqn',
                label = 'vega'
            )
        else:
            return NimbleISCSIInitiator(
        )
        """

    def testNimbleISCSIInitiator(self):
        """Test NimbleISCSIInitiator"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
