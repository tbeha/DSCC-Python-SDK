# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4system_settings_details_system_parameters import DeviceType4systemSettingsDetailsSystemParameters

class TestDeviceType4systemSettingsDetailsSystemParameters(unittest.TestCase):
    """DeviceType4systemSettingsDetailsSystemParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4systemSettingsDetailsSystemParameters:
        """Test DeviceType4systemSettingsDetailsSystemParameters
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4systemSettingsDetailsSystemParameters`
        """
        model = DeviceType4systemSettingsDetailsSystemParameters()
        if include_optional:
            return DeviceType4systemSettingsDetailsSystemParameters(
                fc_raw_space_alert = 1,
                max_volume_retention = 1209600,
                overprov_ratio_limit = 0,
                overprov_ratio_warning = 0
            )
        else:
            return DeviceType4systemSettingsDetailsSystemParameters(
        )
        """

    def testDeviceType4systemSettingsDetailsSystemParameters(self):
        """Test DeviceType4systemSettingsDetailsSystemParameters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
