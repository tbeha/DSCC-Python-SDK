# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_shelf_details import NimbleShelfDetails

class TestNimbleShelfDetails(unittest.TestCase):
    """NimbleShelfDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleShelfDetails:
        """Test NimbleShelfDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleShelfDetails`
        """
        model = NimbleShelfDetails()
        if include_optional:
            return NimbleShelfDetails(
                associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817","type":"storage-systems"}],
                chassis_sensors = [
                    dscc.models.nimble_ns_shelf_sensor.NimbleNsShelfSensor(
                        cid = 'A', 
                        display_name = 'motherboard', 
                        location = 'motherboard', 
                        name = 'motherboard', 
                        status = 'OK', 
                        type = 'fan', 
                        value = 23, )
                    ],
                chassis_type = 'chassis_4u24',
                common_resource_attributes = dscc.models.nimble_common_resource_attributes.NimbleCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'null',
                ctrlrs = [
                    dscc.models.nimble_ns_shelf_ctrlr.NimbleNsShelfCtrlr(
                        cached_serial = 'cs-18bb66', 
                        ctrlr_attrset_list = [
                            dscc.models.nimble_ns_shelf_ctrlr_attr_set.NimbleNsShelfCtrlrAttrSet(
                                cached_serial = 'AA-100373', 
                                disk_serials = 'disk_sdf:2:0:0:0,disk_sdg:2:0:1:0,disk_sdh:2:0:2:0,disk_sdi:2:0:3:0,disk_sdj:2:0:4:0,disk_sdk:2:0:5:0,disk_sdb:1:0:0:0,disk_sdc:1:0:1:0,disk_sdd:1:0:2:0,disk_sde:1:0:3:0,disk_sdl:2:0:6:0,disk_sdm:2:0:8:0,disk_sdn:2:0:9:0,disk_sdo:2:0:10:0,disk_sdp:2:0:11:0,disk_sdq:2:0:12:0', 
                                disk_types = 'WD-WCAW31074925,WD-WCAW31562278,WD-WCAW31543481,WD-WCAW31546957,CVPO105101AQ080JGN,CVPO1051023B080JGN,WD-WCAW31507140,WD-WCAW31545053,WD-WCAW31549016,WD-WCAW31544371', 
                                hw_state = 'ready', 
                                session_serial = 'shelf_0_0x5003048000b0567f_1456884624.213307', 
                                sw_type = 'Disk Shelf', )
                            ], 
                        ctrlr_hw_model = 'head_x8', 
                        ctrlr_sensor_last_run = 0, 
                        ctrlr_sensors = [
                            dscc.models.nimble_ns_shelf_sensor.NimbleNsShelfSensor(
                                cid = 'A', 
                                display_name = 'motherboard', 
                                location = 'motherboard', 
                                name = 'motherboard', 
                                status = 'OK', 
                                type = 'fan', 
                                value = 23, )
                            ], 
                        ctrlr_side = 'A', 
                        enc_loc_id = 0, 
                        exp_sas_addr = '0x5003048000b0567f', 
                        extra_attributes = [
                            ''
                            ], 
                        fan_overall_status = 'Missing', 
                        hw_master_state = 'master', 
                        hw_mship_failure = False, 
                        identify_status = False, 
                        port_info = [
                            dscc.models.nimble_ns_shelf_port_info.NimbleNsShelfPortInfo(
                                port_errors = '', 
                                port_idx = 0, 
                                port_name = 'SAS PORT1', 
                                port_status = 'disconnected', 
                                port_type = 'downstream', 
                                remote_loc_id = 4294967295, 
                                remote_port_id = 4294967295, 
                                remote_sas_addr = '', 
                                remote_sas_domain = 'A', 
                                remote_sas_phy_id = '', )
                            ], 
                        psu_overall_status = 'Failed', 
                        sw_master_state = 'release master', 
                        temp_overall_status = 'Missing', )
                    ],
                customer_id = 'string',
                disk_sets = [
                    dscc.models.nimble_ns_disk_set_attr.NimbleNsDiskSetAttr(
                        ave_mb_ps = 0, 
                        ave_segment_ps = 0, 
                        ave_ttc = 0, 
                        driveset = 0, 
                        is_capacity_valid = False, 
                        is_flash_shelf = False, 
                        pause_state = 0, 
                        pct_completion = 0, 
                        raw_cache_capacity = 34359738368, 
                        raw_capacity = 476741369856, 
                        sw_state = 'online', 
                        usable_cache_capacity = 244695092429, 
                        usable_capacity = 244695092429, )
                    ],
                fan_overall_status = 'Failed',
                generation = 0,
                model_ext = 'CS210-8T-160F',
                psu_overall_status = 'Failed',
                resource_uri = '/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817',
                temp_overall_status = 'Failed',
                type = 'string'
            )
        else:
            return NimbleShelfDetails(
        )
        """

    def testNimbleShelfDetails(self):
        """Test NimbleShelfDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
