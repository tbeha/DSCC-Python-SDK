# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_enclosures_detailed_fields_enclosure_cards import DeviceType4EnclosuresDetailedFieldsEnclosureCards

class TestDeviceType4EnclosuresDetailedFieldsEnclosureCards(unittest.TestCase):
    """DeviceType4EnclosuresDetailedFieldsEnclosureCards unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4EnclosuresDetailedFieldsEnclosureCards:
        """Test DeviceType4EnclosuresDetailedFieldsEnclosureCards
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4EnclosuresDetailedFieldsEnclosureCards`
        """
        model = DeviceType4EnclosuresDetailedFieldsEnclosureCards()
        if include_optional:
            return DeviceType4EnclosuresDetailedFieldsEnclosureCards(
                items = [
                    dscc.models.device_type4enclosure_card_details.DeviceType4enclosureCardDetails(
                        customer_id = 'string', 
                        dcsdata = dscc.models.device_type4ec_dcsdata.DeviceType4ecDcsdata(
                            fw_status = '', 
                            fw_version = '', 
                            master = True, 
                            sas_status = '', ), 
                        displayname = '', 
                        domain = '', 
                        element_status_code = '', 
                        enclosure_card_id = 0, 
                        enclosure_id = 1, 
                        enclosure_name = '', 
                        enclosure_type = 'ENCLOSURE_DCS8', 
                        enclosure_uid = '9c3c4f29a82fd8d632ff379116fa0b8f', 
                        fail_indicator = False, 
                        generation = 0, 
                        id = '9c3c4f29a82fd8d632ff379116fa0b8f', 
                        is_node_card = False, 
                        locate_enabled = False, 
                        locate_seven_seg_display = '', 
                        loop_a = False, 
                        loop_b = False, 
                        manufacturing = dscc.models.device_type4_manufacturing_single.DeviceType4ManufacturingSingle(
                            assembly_rev = '002*', 
                            check_sum = '--', 
                            hpe_model_name = 'HPE 3PAR 600 2S Node', 
                            manufacturer = 'XYRATEX', 
                            model = '0974244-06', 
                            saleable_part_number = '0974244-06', 
                            saleable_serial_number = '4UW0002941', 
                            serial_number = 'PMW0974244G4T88', 
                            spare_part_number = 'P04031-001', ), 
                        name = 'SASB', 
                        resource_uri = '/v1/storage-systems/device-type4/2FF70002AC018D94/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-cards/8621946048c1cb24bdfc57e9b3b460ac', 
                        safe_to_remove = False, 
                        seven_seg_display = '', 
                        state = dscc.models.device_type4_state.DeviceType4State(
                            detailed = [
                                ''
                                ], 
                            overall = 'STATE_NORMAL', ), 
                        system_id = '7CE751P312', 
                        type = 'string', )
                    ],
                page_limit = 1,
                page_offset = 1,
                total = 1
            )
        else:
            return DeviceType4EnclosuresDetailedFieldsEnclosureCards(
        )
        """

    def testDeviceType4EnclosuresDetailedFieldsEnclosureCards(self):
        """Test DeviceType4EnclosuresDetailedFieldsEnclosureCards"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
