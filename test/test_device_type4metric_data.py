# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4metric_data import DeviceType4metricData

class TestDeviceType4metricData(unittest.TestCase):
    """DeviceType4metricData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4metricData:
        """Test DeviceType4metricData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4metricData`
        """
        model = DeviceType4metricData()
        if include_optional:
            return DeviceType4metricData(
                items = [
                    dscc.models.device_type4metric_series_rd_wr_data.DeviceType4metricSeriesRdWrData(
                        name = 'appset1', 
                        read_value = 46, 
                        timestampms = 1605063600, 
                        write_value = 23.76, )
                    ],
                total = 1
            )
        else:
            return DeviceType4metricData(
        )
        """

    def testDeviceType4metricData(self):
        """Test DeviceType4metricData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
