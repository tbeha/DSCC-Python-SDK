# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.history_data import HistoryData

class TestHistoryData(unittest.TestCase):
    """HistoryData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HistoryData:
        """Test HistoryData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HistoryData`
        """
        model = HistoryData()
        if include_optional:
            return HistoryData(
                iops_metrics_data = dscc.models.historical_metric_data.historicalMetricData(
                    items = [
                        dscc.models.metric_series_data.metricSeriesData(
                            read_value = 46, 
                            timestampms = 1605063600, 
                            total_value = 89.76, 
                            write_value = 23.76, )
                        ], 
                    total = 1, ),
                iosz_metrics_data_kbs = dscc.models.historical_metric_data.historicalMetricData(
                    items = [
                        dscc.models.metric_series_data.metricSeriesData(
                            read_value = 46, 
                            timestampms = 1605063600, 
                            total_value = 89.76, 
                            write_value = 23.76, )
                        ], 
                    total = 1, ),
                latency_metrics_data_ms = dscc.models.historical_metric_data.historicalMetricData(
                    items = [
                        dscc.models.metric_series_data.metricSeriesData(
                            read_value = 46, 
                            timestampms = 1605063600, 
                            total_value = 89.76, 
                            write_value = 23.76, )
                        ], 
                    total = 1, ),
                qlen_metrics_data = dscc.models.qlen_metric_data_value.qlenMetricDataValue(
                    items = [
                        dscc.models.qlen_metric_series_data_value.qlenMetricSeriesDataValue(
                            timestampms = 1605063600, 
                            value = 46, )
                        ], 
                    total = 1, ),
                throughput_metrics_data_kbps = dscc.models.historical_metric_data.historicalMetricData(
                    items = [
                        dscc.models.metric_series_data.metricSeriesData(
                            read_value = 46, 
                            timestampms = 1605063600, 
                            total_value = 89.76, 
                            write_value = 23.76, )
                        ], 
                    total = 1, )
            )
        else:
            return HistoryData(
        )
        """

    def testHistoryData(self):
        """Test HistoryData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
