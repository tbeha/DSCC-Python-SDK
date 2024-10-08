# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_system_latency_factors_latency_bands import DeviceType4SystemLatencyFactorsLatencyBands

class TestDeviceType4SystemLatencyFactorsLatencyBands(unittest.TestCase):
    """DeviceType4SystemLatencyFactorsLatencyBands unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4SystemLatencyFactorsLatencyBands:
        """Test DeviceType4SystemLatencyFactorsLatencyBands
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4SystemLatencyFactorsLatencyBands`
        """
        model = DeviceType4SystemLatencyFactorsLatencyBands()
        if include_optional:
            return DeviceType4SystemLatencyFactorsLatencyBands(
                read = [
                    dscc.models.device_type4_system_latency_factors_latency_bands_read_inner.DeviceType4SystemLatencyFactors_latencyBands_read_inner(
                        end_time = 1669880791, 
                        start_time = 1669880791, 
                        top_factors = [
                            ''
                            ], )
                    ],
                write = [
                    dscc.models.device_type4_system_latency_factors_latency_bands_write_inner.DeviceType4SystemLatencyFactors_latencyBands_write_inner(
                        end_time = 1669880791, 
                        start_time = 1669880791, 
                        top_factors = [
                            ''
                            ], )
                    ]
            )
        else:
            return DeviceType4SystemLatencyFactorsLatencyBands(
        )
        """

    def testDeviceType4SystemLatencyFactorsLatencyBands(self):
        """Test DeviceType4SystemLatencyFactorsLatencyBands"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
