# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_performance_history_data_history_data import DeviceType4PerformanceHistoryDataHistoryData

class TestDeviceType4PerformanceHistoryDataHistoryData(unittest.TestCase):
    """DeviceType4PerformanceHistoryDataHistoryData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4PerformanceHistoryDataHistoryData:
        """Test DeviceType4PerformanceHistoryDataHistoryData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4PerformanceHistoryDataHistoryData`
        """
        model = DeviceType4PerformanceHistoryDataHistoryData()
        if include_optional:
            return DeviceType4PerformanceHistoryDataHistoryData(
                avgbusy_metrics_data_perct = [
                    dscc.models.device_type4metric_history_data_single_value.DeviceType4metricHistoryDataSingleValue(
                        chart_legend_id = 'VV_NAME-vvname1:HOST_NAME-host:LUN-lun', 
                        time_series_data = dscc.models.device_type4metric_data_value.DeviceType4metricDataValue(
                            items = [
                                dscc.models.device_type4metric_series_data_value.DeviceType4metricSeriesDataValue(
                                    name = 'appset1', 
                                    timestampms = 1605063600, 
                                    value = 46, )
                                ], 
                            total = 1, ), )
                    ],
                iops_metrics_data = [
                    dscc.models.device_type4metric_history_data.DeviceType4metricHistoryData(
                        chart_legend_id = 'VV_NAME-vvname1:HOST_NAME-host:LUN-lun', 
                        time_series_data = dscc.models.device_type4metric_data.DeviceType4metricData(
                            items = [
                                dscc.models.device_type4metric_series_rd_wr_data.DeviceType4metricSeriesRdWrData(
                                    name = 'appset1', 
                                    read_value = 46, 
                                    timestampms = 1605063600, 
                                    write_value = 23.76, )
                                ], 
                            total = 1, ), )
                    ],
                iosz_metrics_data_kbs = [
                    dscc.models.device_type4metric_history_data.DeviceType4metricHistoryData(
                        chart_legend_id = 'VV_NAME-vvname1:HOST_NAME-host:LUN-lun', 
                        time_series_data = dscc.models.device_type4metric_data.DeviceType4metricData(
                            items = [
                                dscc.models.device_type4metric_series_rd_wr_data.DeviceType4metricSeriesRdWrData(
                                    name = 'appset1', 
                                    read_value = 46, 
                                    timestampms = 1605063600, 
                                    write_value = 23.76, )
                                ], 
                            total = 1, ), )
                    ],
                latency_metrics_data_ms = [
                    dscc.models.device_type4metric_history_data.DeviceType4metricHistoryData(
                        chart_legend_id = 'VV_NAME-vvname1:HOST_NAME-host:LUN-lun', 
                        time_series_data = dscc.models.device_type4metric_data.DeviceType4metricData(
                            items = [
                                dscc.models.device_type4metric_series_rd_wr_data.DeviceType4metricSeriesRdWrData(
                                    name = 'appset1', 
                                    read_value = 46, 
                                    timestampms = 1605063600, 
                                    write_value = 23.76, )
                                ], 
                            total = 1, ), )
                    ],
                qlen_metrics_data = [
                    dscc.models.device_type4metric_history_data_single_value.DeviceType4metricHistoryDataSingleValue(
                        chart_legend_id = 'VV_NAME-vvname1:HOST_NAME-host:LUN-lun', 
                        time_series_data = dscc.models.device_type4metric_data_value.DeviceType4metricDataValue(
                            items = [
                                dscc.models.device_type4metric_series_data_value.DeviceType4metricSeriesDataValue(
                                    name = 'appset1', 
                                    timestampms = 1605063600, 
                                    value = 46, )
                                ], 
                            total = 1, ), )
                    ],
                throughput_metrics_data_kbps = [
                    dscc.models.device_type4metric_history_data.DeviceType4metricHistoryData(
                        chart_legend_id = 'VV_NAME-vvname1:HOST_NAME-host:LUN-lun', 
                        time_series_data = dscc.models.device_type4metric_data.DeviceType4metricData(
                            items = [
                                dscc.models.device_type4metric_series_rd_wr_data.DeviceType4metricSeriesRdWrData(
                                    name = 'appset1', 
                                    read_value = 46, 
                                    timestampms = 1605063600, 
                                    write_value = 23.76, )
                                ], 
                            total = 1, ), )
                    ]
            )
        else:
            return DeviceType4PerformanceHistoryDataHistoryData(
        )
        """

    def testDeviceType4PerformanceHistoryDataHistoryData(self):
        """Test DeviceType4PerformanceHistoryDataHistoryData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
