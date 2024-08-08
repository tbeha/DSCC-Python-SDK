# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.node_card_list import NodeCardList

class TestNodeCardList(unittest.TestCase):
    """NodeCardList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeCardList:
        """Test NodeCardList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeCardList`
        """
        model = NodeCardList()
        if include_optional:
            return NodeCardList(
                associated_links = [{"resourceUri":"/v1/storage-systems/device-type1/2FF70002AC018D94/node/e9d353bf98fc1a6bdb90b824e3ca14b5","type":"node"}],
                common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                customer_id = 'string',
                displayname = 'NODE_CARD_NAME',
                domain = '',
                fw_version = '10.10.03.00',
                generation = 0,
                id = '9aeec8a12315995e1efc340a79b6b5bd',
                locate_enabled = False,
                manufacturing = dscc.models.manufacturing_single.manufacturingSingle(
                    assembly_rev = '002*', 
                    check_sum = '--', 
                    hpe_model_name = 'HPE 3PAR 600 2S Node', 
                    manufacturer = 'XYRATEX', 
                    model = '0974244-06', 
                    saleable_part_number = '0974244-06', 
                    saleable_serial_number = '4UW0002941', 
                    serial_number = 'PMW0974244G4T88', 
                    spare_part_number = 'P04031-001', ),
                name = '0:1',
                node_card_type = 'pcicard_type-5',
                node_device_id = 0,
                node_id = 'e9d353bf98fc1a6bdb90b824e3ca14b5',
                resource_uri = '/v1/storage-systems/device-type1/2FF70002AC018D94/nodes/e9d353bf98fc1a6bdb90b824e3ca14b5/node-cards/9aeec8a12315995e1efc340a79b6b5bd',
                revision = '02',
                safe_to_remove = False,
                service_led = 'LED_UNKNOWN',
                slot = 1,
                system_id = '7CE751P312',
                type = 'string'
            )
        else:
            return NodeCardList(
        )
        """

    def testNodeCardList(self):
        """Test NodeCardList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
