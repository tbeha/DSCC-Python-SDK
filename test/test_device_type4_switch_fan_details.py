# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_switch_fan_details import DeviceType4SwitchFanDetails

class TestDeviceType4SwitchFanDetails(unittest.TestCase):
    """DeviceType4SwitchFanDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4SwitchFanDetails:
        """Test DeviceType4SwitchFanDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4SwitchFanDetails`
        """
        model = DeviceType4SwitchFanDetails()
        if include_optional:
            return DeviceType4SwitchFanDetails(
                associated_links = [{"resourceUri":"/v1/storage-systems/device-type4/2FF70002AC01F0FF","type":"systems"},{"resourceUri":"/v1/storage-systems/device-type4/2FF70002AC01F0FF/switches/9c3c4f29a82fd8d632ff379116fa0b8f","type":"switches"}],
                common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'data-ops-manager/storage-systems/device-type4/SGH014XGSP/switches/9c3c4f29a82fd8d632ff379116fa0b8f/switch-fans/8621946048c1cb24bdfc57e9b3b460ac',
                customer_id = 'string',
                displayname = 'Fan 5',
                domain = 'switch',
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
                name = 'Tray-1/5/1',
                request_uri = '/v1/storage-systems/device-type4/2FF70002AC018D94/switches/9c3c4f29a82fd8d632ff379116fa0b8f/switch-fans/8621946048c1cb24bdfc57e9b3b460ac',
                resource_uri = '/v1/storage-systems/device-type4/2FF70002AC018D94/switches/9c3c4f29a82fd8d632ff379116fa0b8f/switch-fans/8621946048c1cb24bdfc57e9b3b460ac',
                speed_a = 'normal',
                speed_b = 'normal',
                state = dscc.models.device_type4_state.DeviceType4State(
                    detailed = [
                        ''
                        ], 
                    overall = 'STATE_NORMAL', ),
                state_a = dscc.models.device_type4_state.DeviceType4State(
                    detailed = [
                        ''
                        ], 
                    overall = 'STATE_NORMAL', ),
                state_b = dscc.models.device_type4_state.DeviceType4State(
                    detailed = [
                        ''
                        ], 
                    overall = 'STATE_NORMAL', ),
                switch_fan_id = 1,
                switch_name = 'sw1',
                switch_uid = '2bc9220b01fae89ef88f10994394b180',
                system_id = '7CE751P312',
                type = 'string'
            )
        else:
            return DeviceType4SwitchFanDetails(
        )
        """

    def testDeviceType4SwitchFanDetails(self):
        """Test DeviceType4SwitchFanDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
