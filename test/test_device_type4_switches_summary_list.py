# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_switches_summary_list import DeviceType4SwitchesSummaryList

class TestDeviceType4SwitchesSummaryList(unittest.TestCase):
    """DeviceType4SwitchesSummaryList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4SwitchesSummaryList:
        """Test DeviceType4SwitchesSummaryList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4SwitchesSummaryList`
        """
        model = DeviceType4SwitchesSummaryList()
        if include_optional:
            return DeviceType4SwitchesSummaryList(
                items = [
                    dscc.models.device_type4_switch_list.DeviceType4SwitchList(
                        active_ip_address = '16.1.9.251', 
                        associated_links = [{"resourceUri":"/v1/storage-systems/device-type4/2FF70002AC01F0FF","type":"systems"}], 
                        common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                            cloud_state = 'CONNECTED', ), 
                        customer_id = 'string', 
                        dhcp_servers = [
                            dscc.models.switch_device_dhcp_server_inner.SwitchDeviceDHCPServer_inner(
                                status = 'operational', 
                                vrf_name = 'inband', )
                            ], 
                        displayname = 'Switch sw2', 
                        domain = 'switch', 
                        fan_state = dscc.models.device_type4_state.DeviceType4State(
                            detailed = [
                                ''
                                ], 
                            overall = 'STATE_NORMAL', ), 
                        fw_version = 'GL.10.11.0001', 
                        generation = 0, 
                        id = '9c3c4f29a82fd8d632ff379116fa0b8f', 
                        locate_enabled = False, 
                        mac_address = '90:20:c2:c2:35:00', 
                        manufacturing = dscc.models.device_type4manufacturing.DeviceType4manufacturing(
                            assembly_rev = '002*', 
                            check_sum = '--', 
                            hpe_model_name = 'HPE 3PAR 600 2S Node', 
                            manufacturer = 'XYRATEX', 
                            model = '0974244-06', 
                            saleable_part_number = '0974244-06', 
                            saleable_serial_number = '4UW0002941', 
                            serial_number = 'PMW0974244G4T88', 
                            spare_part_number = 'P04031-001', ), 
                        mode = 'online', 
                        name = 'sw1', 
                        primary_path = 'Active', 
                        ps1_state = dscc.models.device_type4_state.DeviceType4State(
                            overall = 'STATE_NORMAL', ), 
                        ps2_state = , 
                        resource_uri = '/v1/storage-systems/device-type4/2FF70002AC018D94/switches/8621946048c1cb24bdfc57e9b3b460ac', 
                        secondary_path = 'Inactive', 
                        state = , 
                        switch_id = 1, 
                        system_id = '7CE751P312', 
                        temperature_detail = 'online', 
                        temperature_state = , 
                        type = 'string', 
                        vlans = [
                            dscc.models.switch_device_vlan_inner.SwitchDeviceVlan_inner(
                                operational_state = 'ok', 
                                vlan_id = 1, 
                                vlan_name = 'DEFAULT_VLAN_1', )
                            ], )
                    ],
                page_limit = 1,
                page_offset = 1,
                request_uri = '/v1/storage-systems/device-type4/2FF70002AC018D94/switches',
                total = 1
            )
        else:
            return DeviceType4SwitchesSummaryList(
        )
        """

    def testDeviceType4SwitchesSummaryList(self):
        """Test DeviceType4SwitchesSummaryList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
