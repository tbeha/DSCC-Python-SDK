# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_port_iscsi_edit import DeviceType4PortISCSIEdit

class TestDeviceType4PortISCSIEdit(unittest.TestCase):
    """DeviceType4PortISCSIEdit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4PortISCSIEdit:
        """Test DeviceType4PortISCSIEdit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4PortISCSIEdit`
        """
        model = DeviceType4PortISCSIEdit()
        if include_optional:
            return DeviceType4PortISCSIEdit(
                label = 'port_123',
                mtu = '1500',
                vlans = [
                    dscc.models.device_type4_port_iscsi_edit_vlans_inner.DeviceType4PortISCSIEdit_vlans_inner(
                        gateway_address = '255.255.255.0', 
                        gateway_address_v6 = '2001:db8:85a3::8a2e:370:7114', 
                        ip_address = '192.168.193.21', 
                        ip_address_v6 = '2001:db8:85a3::8a2e:370:7334', 
                        net_mask = '255.255.255.0', 
                        net_mask_v6 = '12', 
                        send_target_group_tag = 13, 
                        vlan_id = '1234', )
                    ]
            )
        else:
            return DeviceType4PortISCSIEdit(
        )
        """

    def testDeviceType4PortISCSIEdit(self):
        """Test DeviceType4PortISCSIEdit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
