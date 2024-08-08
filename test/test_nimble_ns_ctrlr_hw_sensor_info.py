# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_ns_ctrlr_hw_sensor_info import NimbleNsCtrlrHwSensorInfo

class TestNimbleNsCtrlrHwSensorInfo(unittest.TestCase):
    """NimbleNsCtrlrHwSensorInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleNsCtrlrHwSensorInfo:
        """Test NimbleNsCtrlrHwSensorInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleNsCtrlrHwSensorInfo`
        """
        model = NimbleNsCtrlrHwSensorInfo()
        if include_optional:
            return NimbleNsCtrlrHwSensorInfo(
                ctrlr_owner = 'independent',
                current_reading = 56,
                display_name = 'sensor-1',
                location = 'left rear',
                name = 'sensor-1',
                state = 'sensor_ok'
            )
        else:
            return NimbleNsCtrlrHwSensorInfo(
        )
        """

    def testNimbleNsCtrlrHwSensorInfo(self):
        """Test NimbleNsCtrlrHwSensorInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
