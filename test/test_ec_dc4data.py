# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.ec_dc4data import EcDc4data

class TestEcDc4data(unittest.TestCase):
    """EcDc4data unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EcDc4data:
        """Test EcDc4data
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EcDc4data`
        """
        model = EcDc4data()
        if include_optional:
            return EcDc4data(
                hpl_led = 'LED_UNKNOWN',
                split_led = 'LED_UNKNOWN',
                system_led = 'LED_UNKNOWN'
            )
        else:
            return EcDc4data(
        )
        """

    def testEcDc4data(self):
        """Test EcDc4data"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
