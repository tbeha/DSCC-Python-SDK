# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_remove_remote_protection_input_schema import DeviceType4RemoveRemoteProtectionInputSchema

class TestDeviceType4RemoveRemoteProtectionInputSchema(unittest.TestCase):
    """DeviceType4RemoveRemoteProtectionInputSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4RemoveRemoteProtectionInputSchema:
        """Test DeviceType4RemoveRemoteProtectionInputSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4RemoveRemoteProtectionInputSchema`
        """
        model = DeviceType4RemoveRemoteProtectionInputSchema()
        if include_optional:
            return DeviceType4RemoveRemoteProtectionInputSchema(
                partner_id = '29ee132316dc4b05a4805dba13e495ab'
            )
        else:
            return DeviceType4RemoveRemoteProtectionInputSchema(
                partner_id = '29ee132316dc4b05a4805dba13e495ab',
        )
        """

    def testDeviceType4RemoveRemoteProtectionInputSchema(self):
        """Test DeviceType4RemoveRemoteProtectionInputSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
