# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_enclosure_power_details import DeviceType4EnclosurePowerDetails

class TestDeviceType4EnclosurePowerDetails(unittest.TestCase):
    """DeviceType4EnclosurePowerDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4EnclosurePowerDetails:
        """Test DeviceType4EnclosurePowerDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4EnclosurePowerDetails`
        """
        model = DeviceType4EnclosurePowerDetails()
        if include_optional:
            return DeviceType4EnclosurePowerDetails(
                ac_status = '',
                associated_links = [{"resourceUri":"/v1/storage-systems/device-type4/2FF70002AC01F0FF","type":"systems"},{"resourceUri":"/v1/storage-systems/device-type4/2FF70002AC01F0FF/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f","type":"enclosures"}],
                common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'data-ops-manager/storage-systems/device-type4/SGH014XGSP/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-powers/8621946048c1cb24bdfc57e9b3b460ac',
                customer_id = 'string',
                dc_status = '',
                displayname = '',
                domain = '',
                element_status_code = '',
                enclosure_id = 1,
                enclosure_name = '',
                enclosure_power_id = 0,
                enclosure_power_supply_id = 0,
                enclosure_type = 'ENCLOSURE_DCS8',
                enclosure_uid = '9c3c4f29a82fd8d632ff379116fa0b8f',
                fail_indicator = False,
                fail_input = False,
                fail_output = False,
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
                model_read_only = False,
                name = 'SASB',
                request_uri = '/v1/storage-systems/device-type4/2FF70002AC018D94/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-powers/8621946048c1cb24bdfc57e9b3b460ac',
                resource_uri = '/v1/storage-systems/device-type4/2FF70002AC018D94/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/enclosure-powers/8621946048c1cb24bdfc57e9b3b460ac',
                safe_to_remove = False,
                state = dscc.models.device_type4_state.DeviceType4State(
                    detailed = [
                        ''
                        ], 
                    overall = 'STATE_NORMAL', ),
                system_id = '7CE751P312',
                type = 'string'
            )
        else:
            return DeviceType4EnclosurePowerDetails(
        )
        """

    def testDeviceType4EnclosurePowerDetails(self):
        """Test DeviceType4EnclosurePowerDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
