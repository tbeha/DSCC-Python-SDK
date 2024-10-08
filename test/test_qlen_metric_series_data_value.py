# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.qlen_metric_series_data_value import QlenMetricSeriesDataValue

class TestQlenMetricSeriesDataValue(unittest.TestCase):
    """QlenMetricSeriesDataValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QlenMetricSeriesDataValue:
        """Test QlenMetricSeriesDataValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QlenMetricSeriesDataValue`
        """
        model = QlenMetricSeriesDataValue()
        if include_optional:
            return QlenMetricSeriesDataValue(
                timestampms = 1605063600,
                value = 46
            )
        else:
            return QlenMetricSeriesDataValue(
        )
        """

    def testQlenMetricSeriesDataValue(self):
        """Test QlenMetricSeriesDataValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
