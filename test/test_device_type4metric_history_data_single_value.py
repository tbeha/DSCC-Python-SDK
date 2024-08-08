# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4metric_history_data_single_value import DeviceType4metricHistoryDataSingleValue

class TestDeviceType4metricHistoryDataSingleValue(unittest.TestCase):
    """DeviceType4metricHistoryDataSingleValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4metricHistoryDataSingleValue:
        """Test DeviceType4metricHistoryDataSingleValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4metricHistoryDataSingleValue`
        """
        model = DeviceType4metricHistoryDataSingleValue()
        if include_optional:
            return DeviceType4metricHistoryDataSingleValue(
                chart_legend_id = 'VV_NAME-vvname1:HOST_NAME-host:LUN-lun',
                time_series_data = dscc.models.device_type4metric_data_value.DeviceType4metricDataValue(
                    items = [
                        dscc.models.device_type4metric_series_data_value.DeviceType4metricSeriesDataValue(
                            name = 'appset1', 
                            timestampms = 1605063600, 
                            value = 46, )
                        ], 
                    total = 1, )
            )
        else:
            return DeviceType4metricHistoryDataSingleValue(
        )
        """

    def testDeviceType4metricHistoryDataSingleValue(self):
        """Test DeviceType4metricHistoryDataSingleValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
