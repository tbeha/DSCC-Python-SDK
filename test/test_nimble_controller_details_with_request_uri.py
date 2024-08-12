# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_controller_details_with_request_uri import NimbleControllerDetailsWithRequestUri

class TestNimbleControllerDetailsWithRequestUri(unittest.TestCase):
    """NimbleControllerDetailsWithRequestUri unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleControllerDetailsWithRequestUri:
        """Test NimbleControllerDetailsWithRequestUri
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleControllerDetailsWithRequestUri`
        """
        model = NimbleControllerDetailsWithRequestUri()
        if include_optional:
            return NimbleControllerDetailsWithRequestUri(
                request_uri = 'api/v1/storage-systems/devicetype2/2a0df0fe6f7dc7bb16000000000000000000004817/controllers/2a0df0fe6f7dc7bb16000000000000000000004007',
                array_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                array_name = 'myobject-5',
                id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                name = 'A',
                serial = 'AC-109084',
                associated_links = [{resourceUri=/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817, type=storage-systems}],
                asup_time = 0,
                common_resource_attributes = dscc.models.nimble_common_resource_attributes.NimbleCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'null',
                ctrlr_side = 'A',
                customer_id = 'string',
                fan_status = 'fan_okay',
                fans = [
                    dscc.models.nimble_ns_ctrlr_hw_sensor_info.NimbleNsCtrlrHwSensorInfo(
                        ctrlr_owner = 'independent', 
                        current_reading = 56, 
                        display_name = 'sensor-1', 
                        location = 'left rear', 
                        name = 'sensor-1', 
                        state = 'sensor_ok', )
                    ],
                generation = 0,
                hostname = 'myobject-5-A',
                nvme_cards = [
                    dscc.models.nimble_ns_ctrlr_nvme_card.NimbleNsCtrlrNvmeCard(
                        serial_number = 'AC-109084', 
                        size = 56, 
                        state = 'valid', )
                    ],
                nvme_cards_enabled = 56,
                partial_response_ok = True,
                partition_status = [
                    dscc.models.nimble_ns_ctrlr_raid_info.NimbleNsCtrlrRaidInfo(
                        cur_copies = 56, 
                        is_resyncing = True, 
                        max_copies = 56, 
                        raid_id = 18, 
                        raid_type = 'raid0', )
                    ],
                power_status = 'ps_okay',
                power_supplies = [
                    dscc.models.nimble_ns_ctrlr_hw_sensor_info.NimbleNsCtrlrHwSensorInfo(
                        ctrlr_owner = 'independent', 
                        current_reading = 56, 
                        display_name = 'sensor-1', 
                        location = 'left rear', 
                        name = 'sensor-1', 
                        state = 'sensor_ok', )
                    ],
                resource_uri = '/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817',
                state = 'active',
                support_address = '128.0.0.1',
                support_netmask = '255.255.248.0',
                support_nic = 'eth1',
                temperature_sensors = [
                    dscc.models.nimble_ns_ctrlr_hw_sensor_info.NimbleNsCtrlrHwSensorInfo(
                        ctrlr_owner = 'independent', 
                        current_reading = 56, 
                        display_name = 'sensor-1', 
                        location = 'left rear', 
                        name = 'sensor-1', 
                        state = 'sensor_ok', )
                    ],
                temperature_status = 'temperature_okay',
                type = 'string',
                update_end_time = 3400,
                update_error_code = 'SM_ok',
                update_progress_msg = 'example progress message',
                update_start_time = 3400,
                update_state = 'normal',
                version_current = '5.3.0.0-746508-opt',
                version_rollback = 'v1',
                version_target = 'v1'
            )
        else:
            return NimbleControllerDetailsWithRequestUri(
        )
        """

    def testNimbleControllerDetailsWithRequestUri(self):
        """Test NimbleControllerDetailsWithRequestUri"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
