# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4enclosure_sled_list import DeviceType4enclosureSledList

class TestDeviceType4enclosureSledList(unittest.TestCase):
    """DeviceType4enclosureSledList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4enclosureSledList:
        """Test DeviceType4enclosureSledList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4enclosureSledList`
        """
        model = DeviceType4enclosureSledList()
        if include_optional:
            return DeviceType4enclosureSledList(
                associated_links = [{"resourceUri":"/v1/storage-systems/device-type4/2FF70002AC01F0FF","type":"systems"},{"resourceUri":"/v1/storage-systems/device-type4/2FF70002AC01F0FF/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f","type":"enclosures"}],
                common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                customer_id = 'string',
                dc4data = dscc.models.device_type4es_dc4data.DeviceType4esDc4data(
                    hpl_led = 'LED_UNKNOWN', 
                    left = True, 
                    right = True, 
                    system_led = 'LED_UNKNOWN', ),
                disk_count = 1,
                displayname = '',
                domain = '',
                element_status_code = '',
                enclosure_id = 1,
                enclosure_name = '',
                enclosure_type = 'ENCLOSURE_DCS8',
                enclosure_uid = '9c3c4f29a82fd8d632ff379116fa0b8f',
                fail_indicator = False,
                generation = 0,
                id = '9c3c4f29a82fd8d632ff379116fa0b8f',
                locate_enabled = False,
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
                ok_indicator = False,
                port_bypass_a = False,
                port_bypass_b = False,
                power = False,
                pred_fail_indicator = False,
                protocol = 'SAS',
                resource_uri = '/v1/storage-systems/device-type4/2FF70002AC018D94/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-sleds/8621946048c1cb24bdfc57e9b3b460ac',
                safe_to_remove = False,
                sled_id = 0,
                state_loop_a = dscc.models.device_type4_state.DeviceType4State(
                    detailed = [
                        ''
                        ], 
                    overall = 'STATE_NORMAL', ),
                state_loop_b = dscc.models.device_type4_state.DeviceType4State(
                    detailed = [
                        ''
                        ], 
                    overall = 'STATE_NORMAL', ),
                system_id = '7CE751P312',
                temperature = 30,
                type = 'string',
                wwn = '5000C500997AB7B0'
            )
        else:
            return DeviceType4enclosureSledList(
        )
        """

    def testDeviceType4enclosureSledList(self):
        """Test DeviceType4enclosureSledList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
