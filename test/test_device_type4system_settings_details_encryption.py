# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4system_settings_details_encryption import DeviceType4systemSettingsDetailsEncryption

class TestDeviceType4systemSettingsDetailsEncryption(unittest.TestCase):
    """DeviceType4systemSettingsDetailsEncryption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4systemSettingsDetailsEncryption:
        """Test DeviceType4systemSettingsDetailsEncryption
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4systemSettingsDetailsEncryption`
        """
        model = DeviceType4systemSettingsDetailsEncryption()
        if include_optional:
            return DeviceType4systemSettingsDetailsEncryption(
                backup_saved = False,
                dar_state = 'normal',
                enabled = False,
                failed_disks = 2,
                fips_compliant = 'NotCompliant',
                key_location = 'LKM',
                kmpi_protocols = ["1.1","1.2"],
                licensed = False,
                not_fipspd = 2,
                not_node_sed = 2,
                not_sedpd = 2,
                seq_num = 2,
                server_count = 2,
                server_names = ["server1","server2"],
                server_port = 2,
                server_user = 'Username'
            )
        else:
            return DeviceType4systemSettingsDetailsEncryption(
        )
        """

    def testDeviceType4systemSettingsDetailsEncryption(self):
        """Test DeviceType4systemSettingsDetailsEncryption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
