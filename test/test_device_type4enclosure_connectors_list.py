# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4enclosure_connectors_list import DeviceType4enclosureConnectorsList

class TestDeviceType4enclosureConnectorsList(unittest.TestCase):
    """DeviceType4enclosureConnectorsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4enclosureConnectorsList:
        """Test DeviceType4enclosureConnectorsList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4enclosureConnectorsList`
        """
        model = DeviceType4enclosureConnectorsList()
        if include_optional:
            return DeviceType4enclosureConnectorsList(
                associated_links = [{"resourceUri":"/v1/storage-systems/device-type4/2FF70002AC01F0FF","type":"systems"},{"resourceUri":"/v1/storage-systems/device-type4/2FF70002AC01F0FF/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f","type":"enclosures"}],
                common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                connector = 0,
                current_speed = 'currentSpeed',
                customer_id = 'string',
                disabled = 'disabled',
                displayname = 'display name',
                domain = '',
                element_status_code = dscc.models.device_type4_element_status_code.DeviceType4ElementStatusCode(
                    default = '', 
                    key = '', ),
                enclosure_card_id = 0,
                enclosure_card_pci_uid = 'PCIUID',
                enclosure_card_uid = 'CardUID',
                enclosure_id = 0,
                enclosure_name = 'name',
                enclosure_uid = 'uid',
                generation = 0,
                id = 'id',
                ipv4_address = 'ipv4',
                ipv6_address = 'ipv6',
                label = 'label',
                link_speed = 'speed',
                locate = 'locate',
                mac_address = 'mac',
                node_port = dscc.models.device_type4enclosure_connectors_list_node_port.DeviceType4enclosureConnectorsList_nodePort(
                    node = 1, 
                    port = 1, 
                    slot = 1, ),
                resource_uri = '/v1/storage-systems/device-type4/2FF70002AC018D94/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-connectors/8621946048c1cb24bdfc57e9b3b460ac',
                slot = 0,
                system_id = '4UW0004156',
                type = 'type1',
                type_connection = 'External'
            )
        else:
            return DeviceType4enclosureConnectorsList(
        )
        """

    def testDeviceType4enclosureConnectorsList(self):
        """Test DeviceType4enclosureConnectorsList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
