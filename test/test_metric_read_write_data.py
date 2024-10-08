# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.metric_read_write_data import MetricReadWriteData

class TestMetricReadWriteData(unittest.TestCase):
    """MetricReadWriteData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetricReadWriteData:
        """Test MetricReadWriteData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetricReadWriteData`
        """
        model = MetricReadWriteData()
        if include_optional:
            return MetricReadWriteData(
                items = [
                    dscc.models.metric_series_read_write_data.metricSeriesReadWriteData(
                        name = 'appset1', 
                        read_value = 46, 
                        timestampms = 1605063600, 
                        write_value = 23.76, )
                    ],
                total = 1
            )
        else:
            return MetricReadWriteData(
        )
        """

    def testMetricReadWriteData(self):
        """Test MetricReadWriteData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
