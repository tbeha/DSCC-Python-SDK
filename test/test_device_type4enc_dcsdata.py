# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4enc_dcsdata import DeviceType4encDcsdata

class TestDeviceType4encDcsdata(unittest.TestCase):
    """DeviceType4encDcsdata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4encDcsdata:
        """Test DeviceType4encDcsdata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4encDcsdata`
        """
        model = DeviceType4encDcsdata()
        if include_optional:
            return DeviceType4encDcsdata(
                fw_status = '',
                fw_version = ''
            )
        else:
            return DeviceType4encDcsdata(
        )
        """

    def testDeviceType4encDcsdata(self):
        """Test DeviceType4encDcsdata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
