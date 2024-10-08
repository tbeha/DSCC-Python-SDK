# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4ed_dc4data import DeviceType4edDc4data

class TestDeviceType4edDc4data(unittest.TestCase):
    """DeviceType4edDc4data unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4edDc4data:
        """Test DeviceType4edDc4data
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4edDc4data`
        """
        model = DeviceType4edDc4data()
        if include_optional:
            return DeviceType4edDc4data(
                esi = True,
                esi_status = '',
                system_led = 'LED_UNKNOWN'
            )
        else:
            return DeviceType4edDc4data(
        )
        """

    def testDeviceType4edDc4data(self):
        """Test DeviceType4edDc4data"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
