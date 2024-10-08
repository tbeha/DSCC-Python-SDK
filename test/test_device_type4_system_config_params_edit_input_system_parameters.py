# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_system_config_params_edit_input_system_parameters import DeviceType4SystemConfigParamsEditInputSystemParameters

class TestDeviceType4SystemConfigParamsEditInputSystemParameters(unittest.TestCase):
    """DeviceType4SystemConfigParamsEditInputSystemParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4SystemConfigParamsEditInputSystemParameters:
        """Test DeviceType4SystemConfigParamsEditInputSystemParameters
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4SystemConfigParamsEditInputSystemParameters`
        """
        model = DeviceType4SystemConfigParamsEditInputSystemParameters()
        if include_optional:
            return DeviceType4SystemConfigParamsEditInputSystemParameters(
                overprov_ratio_limit = 2,
                overprov_ratio_warning = 1
            )
        else:
            return DeviceType4SystemConfigParamsEditInputSystemParameters(
        )
        """

    def testDeviceType4SystemConfigParamsEditInputSystemParameters(self):
        """Test DeviceType4SystemConfigParamsEditInputSystemParameters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
