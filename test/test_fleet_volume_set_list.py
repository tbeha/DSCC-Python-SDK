# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.fleet_volume_set_list import FleetVolumeSetList

class TestFleetVolumeSetList(unittest.TestCase):
    """FleetVolumeSetList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FleetVolumeSetList:
        """Test FleetVolumeSetList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FleetVolumeSetList`
        """
        model = FleetVolumeSetList()
        if include_optional:
            return FleetVolumeSetList(
                items = [
                    dscc.models.fleet_volumeset.fleetVolumeset(
                        app_type = 'Oracle Database', 
                        application = '', 
                        associated_links = [
                            dscc.models.associated_links_inner.AssociatedLinks_inner(
                                resource_uri = '', 
                                type = '', )
                            ], 
                        common_resource_attributes = dscc.models.common_resource_attributesfleet.commonResourceAttributesfleet(
                            cloud_state = 'CONNECTED', ), 
                        console_uri = '/block/volumes/device-type2/06510ed8b8ee4fd0c7000000000000000000005927', 
                        customer_id = 'string', 
                        generation = 0, 
                        health_state = '', 
                        host_written_capacity_mi_b = 1.337, 
                        id = '4c74ec5c-ecec-4483-9506-3fb5dc45b5d0', 
                        intrinsic_resource = '', 
                        iops = 1.337, 
                        is_internal = True, 
                        latency = 1.337, 
                        location = '', 
                        members = [
                            ''
                            ], 
                        name = 'snap11', 
                        product_family = 'deviceType1', 
                        provisioned_size_mi_b = 1.337, 
                        resource_uri = '/v1/storage-systems/volume-sets', 
                        size_mi_b = 1.337, 
                        space_warning = 1.337, 
                        sub_type = '', 
                        system_id = '7CE751P312', 
                        thin_savings = '', 
                        through_put = 1.337, 
                        total_reserved_mi_b = 1.337, 
                        type = 'string', 
                        used_capacity_percent = 1.337, 
                        used_size_mi_b = 1.337, 
                        volume_set_id = '', 
                        volume_type = '', 
                        wwn = '', )
                    ],
                page_limit = 1,
                page_offset = 1,
                request_uri = '/api/v1/storage-systems/device-type1/7CE751P312/applicationsets/14dbcb4be4836ff8f012a6d0118ba83a',
                total = 1
            )
        else:
            return FleetVolumeSetList(
        )
        """

    def testFleetVolumeSetList(self):
        """Test FleetVolumeSetList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
