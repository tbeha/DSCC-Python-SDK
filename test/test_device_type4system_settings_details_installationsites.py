# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4system_settings_details_installationsites import DeviceType4systemSettingsDetailsInstallationsites

class TestDeviceType4systemSettingsDetailsInstallationsites(unittest.TestCase):
    """DeviceType4systemSettingsDetailsInstallationsites unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4systemSettingsDetailsInstallationsites:
        """Test DeviceType4systemSettingsDetailsInstallationsites
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4systemSettingsDetailsInstallationsites`
        """
        model = DeviceType4systemSettingsDetailsInstallationsites()
        if include_optional:
            return DeviceType4systemSettingsDetailsInstallationsites(
                city = 'Bangalore',
                company = 'Hewlett Packard Enterprise',
                country = 'India',
                hpe_passport_id = 'annajohn@gmail.com',
                hpe_password = 'password',
                id = '2FF70002AC07E9C6',
                postal_code = '560001',
                set_system_location = False,
                state = 'Karnataka',
                street_address = '7992 Woodland Street',
                support_provider = 'HPE',
                system_id = '7CE751P312'
            )
        else:
            return DeviceType4systemSettingsDetailsInstallationsites(
        )
        """

    def testDeviceType4systemSettingsDetailsInstallationsites(self):
        """Test DeviceType4systemSettingsDetailsInstallationsites"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
