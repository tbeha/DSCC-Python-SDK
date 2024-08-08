# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.volume_performance_drifts import VolumePerformanceDrifts

class TestVolumePerformanceDrifts(unittest.TestCase):
    """VolumePerformanceDrifts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VolumePerformanceDrifts:
        """Test VolumePerformanceDrifts
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VolumePerformanceDrifts`
        """
        model = VolumePerformanceDrifts()
        if include_optional:
            return VolumePerformanceDrifts(
                associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type4/ABC239XFZ9/volumes/60002AC000000000000005B200029834","type":"volumes"},{"resourceUri":"/api/v1/storage-systems/device-type4/ABC239XFZ9/volumes/60002AC000000000000005B200029834/performace-history","type":"performance-history"}],
                drifts_detected = [
                    dscc.models.drifts_detected_inner.driftsDetected_inner(
                        actual_end_time = 1669880791, 
                        actual_start_time = 1669880791, 
                        avg90th_percentile = 0.98, 
                        drift_buckets = [
                            dscc.models.drift_buckets_inner.driftBuckets_inner(
                                bucket_name = 128, 
                                bucket_unit = 'KiB', 
                                magnitude = 1.64, )
                            ], 
                        end_time = 1669880791, 
                        io_type = 'read', 
                        latency_range_unit = 'ms', 
                        max_latency_lower_range = 6, 
                        max_latency_upper_range = 8, 
                        start_time = 1669880791, 
                        updated = True, )
                    ],
                end_time = 1669880791,
                request_uri = '/api/v1/storage-systems/device-type4/ABC239XFZ9/volumes/60002AC000000000000005B200029834/insights/performance-drifts',
                start_time = 1669794391,
                system_id = 'ABC239XFZ9',
                tenant_id = 'fc5f41652a53497e88cdcebc715xxxxx',
                timezone = 'Asia/Calcutta',
                volume_id = '60002AC000000000000005B200029834'
            )
        else:
            return VolumePerformanceDrifts(
        )
        """

    def testVolumePerformanceDrifts(self):
        """Test VolumePerformanceDrifts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
