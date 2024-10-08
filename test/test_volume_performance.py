# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.volume_performance import VolumePerformance

class TestVolumePerformance(unittest.TestCase):
    """VolumePerformance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VolumePerformance:
        """Test VolumePerformance
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VolumePerformance`
        """
        model = VolumePerformance()
        if include_optional:
            return VolumePerformance(
                common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                iops = dscc.models.kpi_metrics.KpiMetrics(
                    read = dscc.models.pm_perf_data.pmPerfData(
                        avg_of1day = 33.65, 
                        avg_of1hour = 40.4, 
                        avg_of8hours = 50.98, 
                        avg_of_latest = 3.4, ), 
                    total = dscc.models.pm_perf_data.pmPerfData(
                        avg_of1day = 33.65, 
                        avg_of1hour = 40.4, 
                        avg_of8hours = 50.98, 
                        avg_of_latest = 3.4, ), 
                    write = , ),
                latency_ms = dscc.models.kpi_metrics.KpiMetrics(
                    read = dscc.models.pm_perf_data.pmPerfData(
                        avg_of1day = 33.65, 
                        avg_of1hour = 40.4, 
                        avg_of8hours = 50.98, 
                        avg_of_latest = 3.4, ), 
                    total = dscc.models.pm_perf_data.pmPerfData(
                        avg_of1day = 33.65, 
                        avg_of1hour = 40.4, 
                        avg_of8hours = 50.98, 
                        avg_of_latest = 3.4, ), 
                    write = , ),
                request_uri = '/v1/storage-systems/device-type1/SGH014XGSP/volumes/a7c4e6593f51d0b98f0e40d7e6df04fd/performance-statistics',
                resource_uri = '/v1/storage-systems/device-type1/SGH014XGSP/volumes/a7c4e6593f51d0b98f0e40d7e6df04fd/performance-statistics',
                throughput_kbps = dscc.models.kpi_metrics.KpiMetrics(
                    read = dscc.models.pm_perf_data.pmPerfData(
                        avg_of1day = 33.65, 
                        avg_of1hour = 40.4, 
                        avg_of8hours = 50.98, 
                        avg_of_latest = 3.4, ), 
                    total = dscc.models.pm_perf_data.pmPerfData(
                        avg_of1day = 33.65, 
                        avg_of1hour = 40.4, 
                        avg_of8hours = 50.98, 
                        avg_of_latest = 3.4, ), 
                    write = , )
            )
        else:
            return VolumePerformance(
        )
        """

    def testVolumePerformance(self):
        """Test VolumePerformance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
