# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.volume_set_proximity_settings import VolumeSetProximitySettings

class TestVolumeSetProximitySettings(unittest.TestCase):
    """VolumeSetProximitySettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VolumeSetProximitySettings:
        """Test VolumeSetProximitySettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VolumeSetProximitySettings`
        """
        model = VolumeSetProximitySettings()
        if include_optional:
            return VolumeSetProximitySettings(
                items = [
                    dscc.models.volume_set_host_group_list.VolumeSetHostGroupList(
                        common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                            cloud_state = 'CONNECTED', ), 
                        customer_id = 'string', 
                        generation = 56, 
                        host_group_name = 'hostset1', 
                        hosts = [
                            dscc.models.volume_set_host_proximity_info.VolumeSetHostProximityInfo(
                                dscc_host_name = 'host1', 
                                host_id = '0af26e4430948dd5c37bea1757107caf', 
                                name = 'host1', 
                                os = 'Windows Server', 
                                proximity = dscc.models.host_proximity_detail.hostProximityDetail(
                                    is_remote_array_support_replication = True, 
                                    is_source_array_support_replication = True, 
                                    local_system = 'CS2-A630-SVQ8', 
                                    proximity_value = 'PRIMARY', 
                                    remote_system = 's2937', ), )
                            ], 
                        system_id = '7CE816P0SR', 
                        type = 'string', )
                    ],
                page_limit = 1,
                page_offset = 1,
                resource_uri = '/api/v1/storage-systems/device-type1/2FF70002AC018D94/applicationsets/9c3c4f29a82fd8d632ff379116fa0b8f/proximity-settings',
                total = 1
            )
        else:
            return VolumeSetProximitySettings(
        )
        """

    def testVolumeSetProximitySettings(self):
        """Test VolumeSetProximitySettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
