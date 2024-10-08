# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_performance_history_data import NimblePerformanceHistoryData

class TestNimblePerformanceHistoryData(unittest.TestCase):
    """NimblePerformanceHistoryData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimblePerformanceHistoryData:
        """Test NimblePerformanceHistoryData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimblePerformanceHistoryData`
        """
        model = NimblePerformanceHistoryData()
        if include_optional:
            return NimblePerformanceHistoryData(
                common_resource_attributes = dscc.models.nimble_common_resource_attributes.NimbleCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                customer_id = 'fc5f41652a53497e88cdcebc715cc1cf',
                end_time = 162564271,
                history_data = dscc.models.nimble_performance_history_data_history_data.nimblePerformanceHistoryData_historyData(
                    iops_metrics_data = [
                        dscc.models.nimble_metric_history_data.nimbleMetricHistoryData(
                            chart_legend_id = 'VolumeName', 
                            resource_id = '001c0920dff4b68c9d000000000000000000000001', 
                            time_series_data = dscc.models.nimble_metric_data.nimbleMetricData(
                                items = [
                                    dscc.models.nimble_metric_perf_series_data.nimbleMetricPerfSeriesData(
                                        name = 'VolumeName', 
                                        read_value = 46, 
                                        timestampms = 1605063600, 
                                        write_value = 23.76, )
                                    ], 
                                total = 1, ), )
                        ], 
                    latency_metrics_data_ms = [
                        dscc.models.nimble_metric_history_data.nimbleMetricHistoryData(
                            chart_legend_id = 'VolumeName', 
                            resource_id = '001c0920dff4b68c9d000000000000000000000001', )
                        ], 
                    throughput_metrics_data_kbps = [
                        
                        ], ),
                request_uri = '/v1/storage-systems/device-type2/0000000110000000/volumes/volume-performance',
                start_time = 1625556314
            )
        else:
            return NimblePerformanceHistoryData(
        )
        """

    def testNimblePerformanceHistoryData(self):
        """Test NimblePerformanceHistoryData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
