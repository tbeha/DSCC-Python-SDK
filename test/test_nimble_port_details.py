# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_port_details import NimblePortDetails

class TestNimblePortDetails(unittest.TestCase):
    """NimblePortDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimblePortDetails:
        """Test NimblePortDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimblePortDetails`
        """
        model = NimblePortDetails()
        if include_optional:
            return NimblePortDetails(
                array_id = '0900000000000004d3000000000000000000000004',
                array_name_or_serial = 'g1a1',
                bus_location = '0000:81:00.0',
                common_resource_attributes = dscc.models.nimble_common_resource_attributes.NimbleCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'null',
                controller_id = 'c300000000000004d3000000000000000400000000',
                controller_name = 'A',
                fabric_info = dscc.models.nimble_fibre_channel_fabric_info.NimbleFibreChannelFabricInfo(
                    fabric_switch_name = 'Switch_A1', 
                    fabric_switch_port = 10, 
                    fabric_switch_port_number = 'fc/15', 
                    fabric_switch_wwnn = 'da:ad:da:ad:da:ad:da:ad', 
                    fabric_switch_wwpn = 'd0:0d:d0:0d:d0:0d:d0:0d', 
                    fabric_wwn = 'fa:b4:1c:fa:b4:1c:fa:b4', 
                    fc_id = '1ceace', 
                    logged_in = True, ),
                fc_port_id = '1f01167316131',
                fc_port_name = 'fc1',
                firmware_version = '1.1.59.0',
                id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                ip_list = dscc.models.ip_list_info.IpListInfo(
                    ip = 'xx.xx.xx', 
                    vlan_id = 1, ),
                is_present = True,
                link_info = dscc.models.nimble_fibre_channel_link_info.NimbleFibreChannelLinkInfo(
                    link_speed = 'link_speed_1000M', 
                    link_status = 'plat_fc_link_status_reset', 
                    max_link_speed = 'link_speed_10000M', 
                    operational_status = 'plat_fc_operational_status_admin_offline', ),
                link_speed = 'link_speed_1000M',
                link_status = 'link_status_up',
                logical_port_number = 0,
                mac = '11:33:55:77:99:BB',
                max_link_speed = 'link_speed_1000M',
                mtu = 1500,
                name = 'interface1.1',
                nic_type = 'nic_type_tp',
                online = True,
                orientation = 'left_to_right',
                partial_response_ok = True,
                peerzone = '',
                port = 0,
                slot = 0,
                wwnn = '56:c9:ce:90:9b:84:c9:00',
                wwpn = '56:c9:ce:90:9b:84:c9:01'
            )
        else:
            return NimblePortDetails(
        )
        """

    def testNimblePortDetails(self):
        """Test NimblePortDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
