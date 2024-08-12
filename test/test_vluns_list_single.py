# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.vluns_list_single import VlunsListSingle

class TestVlunsListSingle(unittest.TestCase):
    """VlunsListSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VlunsListSingle:
        """Test VlunsListSingle
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VlunsListSingle`
        """
        model = VlunsListSingle()
        if include_optional:
            return VlunsListSingle(
                active = True,
                common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'data-ops-manager/storage-systems/device-type1/SGH014XGSP/volumes/{volumeUid}/vluns/{uid}',
                device_wwns = '',
                disk_partition = '',
                displayname = '',
                domain = '',
                failed_path_interval = 1,
                failed_path_policy = '',
                id = '',
                initiators = dscc.models.device_type4_vluns_list_single_initiators.DeviceType4VlunsListSingle_initiators(
                    device_discovered_name = 'TEST11', 
                    id = '6848ef683c27403e96caa51816ddc72c', 
                    resource_uri = '/v1/host-initiators/6848ef683c27403e96caa51816ddc72c', 
                    type = 'host-initiators', ),
                lun = 1,
                mount_point = '',
                mount_point_fsau = 1,
                multi_path_type = '',
                port_pos = dscc.models.device_type4_vluns_list_single_port_pos.DeviceType4VlunsListSingle_portPos(
                    node = 1, 
                    port = 1, 
                    slot = 1, ),
                raw_volume = '',
                remote_name = '',
                request_uri = '- TO BE IMPLEMENTED',
                resource_uri = '- TO BE IMPLEMENTED',
                state = dscc.models.device_type4_vluns_list_single_state.DeviceType4VlunsListSingle_state(
                    detailed = [
                        ''
                        ], 
                    overall = 'STATE_NORMAL', ),
                status = '',
                system_id = '',
                tpg_id = 1,
                type = '',
                used_space = 1,
                volume_group = '',
                volume_manager = '',
                volume_name = '',
                volume_wwn = '',
                vv_reserved_user_space = 1,
                vv_size = 1
            )
        else:
            return VlunsListSingle(
        )
        """

    def testVlunsListSingle(self):
        """Test VlunsListSingle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
