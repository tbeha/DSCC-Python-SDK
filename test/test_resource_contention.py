# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.resource_contention import ResourceContention

class TestResourceContention(unittest.TestCase):
    """ResourceContention unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceContention:
        """Test ResourceContention
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceContention`
        """
        model = ResourceContention()
        if include_optional:
            return ResourceContention(
                associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type4/{uid}","type":"systems"}],
                cpu_contention = dscc.models.resource_contention_data.resourceContentionData(
                    resource_metric_data = [
                        dscc.models.historical_data.historicalData(
                            timestamp_ms = 1669794420000, 
                            value = 0.47, )
                        ], 
                    top_contributors = [
                        dscc.models.resource_contention_contributors.resourceContentionContributors(
                            appset_type = 'Oracle', 
                            prov_type = 'tpvv', 
                            read_latency = 40.25, 
                            read_throughput = 17.25, 
                            total_iops = 22.36, 
                            volume_name = 'VV-S2444-IOPS-1.0', 
                            volume_status = 'Normal', 
                            volume_uid = 'bdce8ba359c68370085e66bf2615c30d', 
                            volume_wwn = '60002AC000000000000000130002AE0B', 
                            write_latency = 85.25, 
                            write_throughput = 20.75, )
                        ], ),
                customer_id = 'fc5f41652a53497e88cdcebc715cc1cf',
                disk_contention = dscc.models.resource_contention_data.resourceContentionData(
                    resource_metric_data = [
                        dscc.models.historical_data.historicalData(
                            timestamp_ms = 1669794420000, 
                            value = 0.47, )
                        ], 
                    top_contributors = [
                        dscc.models.resource_contention_contributors.resourceContentionContributors(
                            appset_type = 'Oracle', 
                            prov_type = 'tpvv', 
                            read_latency = 40.25, 
                            read_throughput = 17.25, 
                            total_iops = 22.36, 
                            volume_name = 'VV-S2444-IOPS-1.0', 
                            volume_status = 'Normal', 
                            volume_uid = 'bdce8ba359c68370085e66bf2615c30d', 
                            volume_wwn = '60002AC000000000000000130002AE0B', 
                            write_latency = 85.25, 
                            write_throughput = 20.75, )
                        ], ),
                end_time = 1669880791,
                request_uri = '/api/v1/storage-systems/device-type4/ABC239XFZ9/insights/resource-contention',
                start_time = 1669794391,
                system_id = 'ABC239XFZ9'
            )
        else:
            return ResourceContention(
        )
        """

    def testResourceContention(self):
        """Test ResourceContention"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
