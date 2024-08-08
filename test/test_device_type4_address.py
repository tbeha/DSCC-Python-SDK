# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_address import DeviceType4Address

class TestDeviceType4Address(unittest.TestCase):
    """DeviceType4Address unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4Address:
        """Test DeviceType4Address
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4Address`
        """
        model = DeviceType4Address()
        if include_optional:
            return DeviceType4Address(
                active_node = 1,
                auto_sense = True,
                full_duplex = True,
                ip_address = '15.12.123.234',
                net_mask = '255.255.255.0',
                speed = 1000,
                state = dscc.models.device_type4_state.DeviceType4State(
                    detailed = [
                        ''
                        ], 
                    overall = 'STATE_NORMAL', ),
                status = 'Active'
            )
        else:
            return DeviceType4Address(
        )
        """

    def testDeviceType4Address(self):
        """Test DeviceType4Address"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
