# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.system_settings_details_system_parameters import SystemSettingsDetailsSystemParameters

class TestSystemSettingsDetailsSystemParameters(unittest.TestCase):
    """SystemSettingsDetailsSystemParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemSettingsDetailsSystemParameters:
        """Test SystemSettingsDetailsSystemParameters
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemSettingsDetailsSystemParameters`
        """
        model = SystemSettingsDetailsSystemParameters()
        if include_optional:
            return SystemSettingsDetailsSystemParameters(
                allow_wrtback_single_node = 7,
                allow_wrtback_upgrade = 7,
                enable_aiqo_s = 'yes',
                fc_raw_space_alert = 1,
                host_dif = 'yes',
                host_dif_template = 'STD_HOST_DIF',
                max_volume_retention = 1209600,
                overprov_ratio_limit = 0,
                overprov_ratio_warning = 0
            )
        else:
            return SystemSettingsDetailsSystemParameters(
        )
        """

    def testSystemSettingsDetailsSystemParameters(self):
        """Test SystemSettingsDetailsSystemParameters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
