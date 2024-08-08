# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_edit_app_set_qos_config_input import DeviceType4EditAppSetQosConfigInput

class TestDeviceType4EditAppSetQosConfigInput(unittest.TestCase):
    """DeviceType4EditAppSetQosConfigInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4EditAppSetQosConfigInput:
        """Test DeviceType4EditAppSetQosConfigInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4EditAppSetQosConfigInput`
        """
        model = DeviceType4EditAppSetQosConfigInput()
        if include_optional:
            return DeviceType4EditAppSetQosConfigInput(
                action = 'ADD_QOS',
                bandwidth_max_limit_ki_b = 100,
                enable = True,
                enable_sr_alert = True,
                iops_max_limit = 1,
                per_tb = True
            )
        else:
            return DeviceType4EditAppSetQosConfigInput(
                action = 'ADD_QOS',
        )
        """

    def testDeviceType4EditAppSetQosConfigInput(self):
        """Test DeviceType4EditAppSetQosConfigInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
