# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_volume_set_host_group_list import DeviceType4VolumeSetHostGroupList

class TestDeviceType4VolumeSetHostGroupList(unittest.TestCase):
    """DeviceType4VolumeSetHostGroupList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4VolumeSetHostGroupList:
        """Test DeviceType4VolumeSetHostGroupList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4VolumeSetHostGroupList`
        """
        model = DeviceType4VolumeSetHostGroupList()
        if include_optional:
            return DeviceType4VolumeSetHostGroupList(
                common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                customer_id = 'string',
                generation = 56,
                host_group_name = 'hostset1',
                hosts = [
                    dscc.models.device_type4_volume_set_host_proximity_info.DeviceType4VolumeSetHostProximityInfo(
                        dscc_host_name = 'host1', 
                        host_id = '0af26e4430948dd5c37bea1757107caf', 
                        name = 'host1', 
                        os = 'Windows Server', 
                        proximity = dscc.models.device_type4host_proximity_detail.DeviceType4hostProximityDetail(
                            is_remote_array_support_replication = True, 
                            is_source_array_support_replication = True, 
                            local_system = 'CS2-A630-SVQ8', 
                            proximity_value = 'PRIMARY', 
                            remote_system = 's2937', ), )
                    ],
                system_id = '7CE816P0SR',
                type = 'string'
            )
        else:
            return DeviceType4VolumeSetHostGroupList(
        )
        """

    def testDeviceType4VolumeSetHostGroupList(self):
        """Test DeviceType4VolumeSetHostGroupList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
