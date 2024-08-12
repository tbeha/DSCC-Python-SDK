# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.volume_latency_annotations import VolumeLatencyAnnotations

class TestVolumeLatencyAnnotations(unittest.TestCase):
    """VolumeLatencyAnnotations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VolumeLatencyAnnotations:
        """Test VolumeLatencyAnnotations
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VolumeLatencyAnnotations`
        """
        model = VolumeLatencyAnnotations()
        if include_optional:
            return VolumeLatencyAnnotations(
                associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type4/ABC239XFZ9/volumes/60002AC000000000000005B200029834","type":"volumes"},{"resourceUri":"/api/v1/storage-systems/device-type4/ABC239XFZ9/volumes/60002AC000000000000005B200029834/performace-history","type":"performance-history"}],
                customer_id = 'fc5f41652a53497e88cdcebc715cc1cf',
                end_time = 1669880791,
                latency_annotations = dscc.models.latency_annotations.latencyAnnotations(
                    read = [
                        dscc.models.latency_annotation_metrics.latencyAnnotationMetrics(
                            latency_qtl90 = 6.21, 
                            max_range = '6ms-8ms', 
                            timestamp_ms = 1669880791, )
                        ], 
                    write = [
                        dscc.models.latency_annotation_metrics.latencyAnnotationMetrics(
                            latency_qtl90 = 6.21, 
                            max_range = '6ms-8ms', 
                            timestamp_ms = 1669880791, )
                        ], ),
                request_uri = '/api/v1/storage-systems/device-type4/ABC239XFZ9/volumes/60002AC000000000000005B200029834/insights/latency-annotations',
                start_time = 1669794391,
                system_id = 'ABC239XFZ9',
                volume_id = '60002AC000000000000005B200029834'
            )
        else:
            return VolumeLatencyAnnotations(
        )
        """

    def testVolumeLatencyAnnotations(self):
        """Test VolumeLatencyAnnotations"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
