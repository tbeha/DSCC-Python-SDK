# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4rx_loss_pin import DeviceType4rxLossPin

class TestDeviceType4rxLossPin(unittest.TestCase):
    """DeviceType4rxLossPin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4rxLossPin:
        """Test DeviceType4rxLossPin
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4rxLossPin`
        """
        model = DeviceType4rxLossPin()
        if include_optional:
            return DeviceType4rxLossPin(
                default = '',
                key = ''
            )
        else:
            return DeviceType4rxLossPin(
        )
        """

    def testDeviceType4rxLossPin(self):
        """Test DeviceType4rxLossPin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
