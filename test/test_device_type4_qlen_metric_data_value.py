# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_qlen_metric_data_value import DeviceType4QlenMetricDataValue

class TestDeviceType4QlenMetricDataValue(unittest.TestCase):
    """DeviceType4QlenMetricDataValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4QlenMetricDataValue:
        """Test DeviceType4QlenMetricDataValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4QlenMetricDataValue`
        """
        model = DeviceType4QlenMetricDataValue()
        if include_optional:
            return DeviceType4QlenMetricDataValue(
                items = [
                    dscc.models.device_type4_qlen_metric_series_data_value.DeviceType4QlenMetricSeriesDataValue(
                        timestampms = 1605063600, 
                        value = 46, )
                    ],
                total = 1
            )
        else:
            return DeviceType4QlenMetricDataValue(
        )
        """

    def testDeviceType4QlenMetricDataValue(self):
        """Test DeviceType4QlenMetricDataValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
