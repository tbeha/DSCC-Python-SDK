# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_enclosure_card_detailed_fields import DeviceType4EnclosureCardDetailedFields

class TestDeviceType4EnclosureCardDetailedFields(unittest.TestCase):
    """DeviceType4EnclosureCardDetailedFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4EnclosureCardDetailedFields:
        """Test DeviceType4EnclosureCardDetailedFields
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4EnclosureCardDetailedFields`
        """
        model = DeviceType4EnclosureCardDetailedFields()
        if include_optional:
            return DeviceType4EnclosureCardDetailedFields(
                associated_links = [{"resourceUri":"/v1/storage-systems/device-type4/2FF70002AC01F0FF","type":"systems"},{"resourceUri":"/v1/storage-systems/device-type4/2FF70002AC01F0FF/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f","type":"enclosures"}],
                common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'data-ops-manager/storage-systems/device-type4/SGH014XGSP/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-cards/8621946048c1cb24bdfc57e9b3b460ac',
                customer_id = 'string',
                dcsdata = dscc.models.device_type4ec_dcsdata.DeviceType4ecDcsdata(
                    fw_status = '', 
                    fw_version = '', 
                    master = True, 
                    sas_status = '', ),
                displayname = '',
                domain = '',
                element_status_code = '',
                enclosure_card_boot_drives = dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_boot_drives.DeviceType4EnclosureCardDetailedFields_enclosureCardBootDrives(
                    items = [
                        dscc.models.device_type4enclosure_card_boot_drive_details.DeviceType4enclosureCardBootDriveDetails(
                            common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                                cloud_state = 'CONNECTED', ), 
                            customer_id = 'string', 
                            displayname = '', 
                            domain = 'stringvalue', 
                            enclosure_card_id = 0, 
                            enclosure_card_uid = '', 
                            enclosure_id = 9, 
                            enclosure_uid = '', 
                            eui_wwn = '', 
                            fw_version = '', 
                            generation = 0, 
                            id = '9c3c4f29a82fd8d632ff379116fa0b8f', 
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
                            path = '', 
                            sed_status = '', 
                            size_mi_b = 56, 
                            slot = 56, 
                            system_id = '7CE751P312', 
                            type = 'string', )
                        ], 
                    page_limit = 1, 
                    page_offset = 1, 
                    total = 1, ),
                enclosure_card_cpu = dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_cpu.DeviceType4EnclosureCardDetailedFields_enclosureCardCpu(
                    items = [
                        dscc.models.device_type4enclosure_card_cpu_details.DeviceType4enclosureCardCpuDetails(
                            bus_speed = 56, 
                            common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                                cloud_state = 'CONNECTED', ), 
                            cpu_cores = 56, 
                            customer_id = 'string', 
                            displayname = '', 
                            domain = '', 
                            enclosure_card_id = 56, 
                            enclosure_card_uid = '', 
                            enclosure_id = 56, 
                            enclosure_uid = '', 
                            generation = 0, 
                            id = '', 
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
                            slot = 56, 
                            speed = 56, 
                            system_id = '', 
                            threads = 56, 
                            type = 'string', )
                        ], 
                    page_limit = 1, 
                    page_offset = 1, 
                    total = 1, ),
                enclosure_card_fan = dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_fan.DeviceType4EnclosureCardDetailedFields_enclosureCardFan(
                    items = [
                        dscc.models.device_type4enclosure_card_fan_details.DeviceType4enclosureCardFanDetails(
                            common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                                cloud_state = 'CONNECTED', ), 
                            customer_id = 'string', 
                            displayname = '', 
                            domain = '', 
                            element_status_code = '', 
                            enclosure_card_fan_id = 0, 
                            enclosure_card_id = 0, 
                            enclosure_card_uid = '9c3c4f29a82fd8d632ff379116fa0b8f', 
                            enclosure_id = 0, 
                            enclosure_name = '', 
                            enclosure_type = 'ENCLOSURE_DCS8', 
                            enclosure_uid = '9c3c4f29a82fd8d632ff379116fa0b8f', 
                            fail_indicator = False, 
                            fan_id = '7CE751P312', 
                            fan_uid = '7CE751P312', 
                            generation = 0, 
                            id = '9c3c4f29a82fd8d632ff379116fa0b8f', 
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
                            speed = '', 
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
                    total = 1, ),
                enclosure_card_id = 0,
                enclosure_card_mem = dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_mem.DeviceType4EnclosureCardDetailedFields_enclosureCardMem(
                    items = [
                        dscc.models.device_type4enclosure_card_memory_details.DeviceType4enclosureCardMemoryDetails(
                            common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                                cloud_state = 'CONNECTED', ), 
                            customer_id = 'string', 
                            displayname = '', 
                            domain = '', 
                            enclosure_card_id = 56, 
                            enclosure_card_mem_type = '', 
                            enclosure_card_uid = '', 
                            enclosure_id = 56, 
                            enclosure_uid = '', 
                            generation = 0, 
                            id = '', 
                            index = 56, 
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
                            name = '', 
                            rcd = '', 
                            size = 56, 
                            speed = 56, 
                            system_id = '', 
                            type = 'string', )
                        ], 
                    page_limit = 1, 
                    page_offset = 1, 
                    total = 1, ),
                enclosure_card_pci = dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_pci.DeviceType4EnclosureCardDetailedFields_enclosureCardPci(
                    items = [
                        dscc.models.device_type4enclosure_card_pci_details.DeviceType4enclosureCardPciDetails(
                            common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                                cloud_state = 'CONNECTED', ), 
                            customer_id = 'string', 
                            displayname = '', 
                            domain = '', 
                            enclosure_card_id = 56, 
                            enclosure_card_pci_type = '', 
                            enclosure_card_uid = '', 
                            enclosure_id = 56, 
                            enclosure_uid = '', 
                            fw_version = '', 
                            generation = 0, 
                            id = '', 
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
                            port_count = 1, 
                            revision = '', 
                            slot = 1, 
                            system_id = '', 
                            type = 'string', )
                        ], 
                    page_limit = 1, 
                    page_offset = 1, 
                    total = 1, ),
                enclosure_card_tpm = dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_tpm.DeviceType4EnclosureCardDetailedFields_enclosureCardTpm(
                    items = [
                        dscc.models.device_type4enclosure_card_tpm_details.DeviceType4enclosureCardTpmDetails(
                            common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                                cloud_state = 'CONNECTED', ), 
                            customer_id = 'string', 
                            displayname = '', 
                            domain = '', 
                            enclosure_card_id = 56, 
                            enclosure_card_tpm_id = 56, 
                            enclosure_card_tpm_type = '', 
                            enclosure_card_uid = '', 
                            enclosure_id = 56, 
                            enclosure_uid = '', 
                            family = '', 
                            fw_version = '', 
                            generation = 0, 
                            id = '', 
                            level = 56, 
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
                            revision = '', 
                            system_id = '', 
                            type = 'string', 
                            vendor = '', )
                        ], 
                    page_limit = 1, 
                    page_offset = 1, 
                    total = 1, ),
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
                request_uri = '/v1/storage-systems/device-type4/2FF70002AC018D94/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-cards/8621946048c1cb24bdfc57e9b3b460ac',
                resource_uri = '/v1/storage-systems/device-type4/2FF70002AC018D94/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-cards/8621946048c1cb24bdfc57e9b3b460ac',
                safe_to_remove = False,
                seven_seg_display = '',
                state = dscc.models.device_type4_state.DeviceType4State(
                    detailed = [
                        ''
                        ], 
                    overall = 'STATE_NORMAL', ),
                system_id = '7CE751P312',
                type = 'string'
            )
        else:
            return DeviceType4EnclosureCardDetailedFields(
        )
        """

    def testDeviceType4EnclosureCardDetailedFields(self):
        """Test DeviceType4EnclosureCardDetailedFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
