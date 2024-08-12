# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_metric_series_data import NimbleMetricSeriesData

class TestNimbleMetricSeriesData(unittest.TestCase):
    """NimbleMetricSeriesData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleMetricSeriesData:
        """Test NimbleMetricSeriesData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleMetricSeriesData`
        """
        model = NimbleMetricSeriesData()
        if include_optional:
            return NimbleMetricSeriesData(
                read_value = 46,
                timestampms = 1605063600,
                total_value = 89.76,
                write_value = 23.76
            )
        else:
            return NimbleMetricSeriesData(
        )
        """

    def testNimbleMetricSeriesData(self):
        """Test NimbleMetricSeriesData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
