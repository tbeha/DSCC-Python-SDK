# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_network_interface_details import NimbleNetworkInterfaceDetails

class TestNimbleNetworkInterfaceDetails(unittest.TestCase):
    """NimbleNetworkInterfaceDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleNetworkInterfaceDetails:
        """Test NimbleNetworkInterfaceDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleNetworkInterfaceDetails`
        """
        model = NimbleNetworkInterfaceDetails()
        if include_optional:
            return NimbleNetworkInterfaceDetails(
                array_name_or_serial = 'myarray',
                controller_id = 'c300000000000004d3000000000000000400000000',
                ip_list = dscc.models.ip_list_info.IpListInfo(
                    ip = 'xx.xx.xx', 
                    vlan_id = 1, ),
                is_present = True,
                link_speed = 'link_speed_1000M',
                link_status = 'link_status_up',
                mac = '11:33:55:77:99:BB',
                max_link_speed = 'link_speed_1000M',
                mtu = 1500,
                nic_type = 'nic_type_tp',
                partial_response_ok = True,
                port = 0,
                slot = 0
            )
        else:
            return NimbleNetworkInterfaceDetails(
        )
        """

    def testNimbleNetworkInterfaceDetails(self):
        """Test NimbleNetworkInterfaceDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
