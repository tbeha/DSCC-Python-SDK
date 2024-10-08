# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.disk_details import DiskDetails

class TestDiskDetails(unittest.TestCase):
    """DiskDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiskDetails:
        """Test DiskDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiskDetails`
        """
        model = DiskDetails()
        if include_optional:
            return DiskDetails(
                admit_time = dscc.models.admit_time.AdmitTime(
                    ms = 1591599192000, 
                    tz = 'Asia/Calcutta', ),
                associated_links = [{"resourceUri":"/v1/storage-systems/device-type1/7CE751P312","type":"systems"},{"resourceUri":"/v1/storage-systems/device-type1/7CE751P312/enclosures/0","type":"enclosures"}],
                capacity = dscc.models.disk_capacity.DiskCapacity(
                    allocated_mi_b = 595968, 
                    failed_mi_b = 0, 
                    free_mi_b = 1233920, 
                    total_mi_b = 595968, 
                    unavailable_mi_b = 0, ),
                common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'data-ops-manager/storage-systems/device-type1/SGH014XGSP/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/disks/d4b13e70924d29afdb77d932f7563ea6',
                consumable_size_mi_b = 1829888,
                customer_id = 'string',
                dev_type = 'DEVTYPE_SSD',
                disk_id = 1,
                displayname = 'Drive 0.SIDE_NONE.2.0',
                domain = '',
                fw_status = '--',
                fw_version = '3P00',
                generation = 0,
                id = 'd4b13e70924d29afdb77d932f7563ea6',
                life_left_pct = 100,
                loop_a0 = dscc.models.disk_loop.DiskLoop(
                    degraded = False, 
                    disabled = False, 
                    port = dscc.models.disk_port_position.diskPortPosition(
                        node = 0, 
                        slot = 0, ), 
                    primary = False, ),
                loop_a1 = dscc.models.disk_loop.DiskLoop(
                    degraded = False, 
                    disabled = False, 
                    port = dscc.models.disk_port_position.diskPortPosition(
                        node = 0, 
                        slot = 0, ), 
                    primary = False, ),
                loop_b0 = dscc.models.disk_loop.DiskLoop(
                    degraded = False, 
                    disabled = False, 
                    port = dscc.models.disk_port_position.diskPortPosition(
                        node = 0, 
                        slot = 0, ), 
                    primary = False, ),
                loop_b1 = dscc.models.disk_loop.DiskLoop(
                    degraded = False, 
                    disabled = False, 
                    port = dscc.models.disk_port_position.diskPortPosition(
                        node = 0, 
                        slot = 0, ), 
                    primary = False, ),
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
                media_type = 'MLC',
                mfg_capacity_gb = 1920,
                position_last = dscc.models.disk_position.DiskPosition(
                    cage = 0, 
                    disk = 0, 
                    side = 'SIDE_NONE', 
                    sled = 2, ),
                position_now = dscc.models.disk_position_now.DiskPositionNow(
                    cage = 0, 
                    disk = 0, 
                    side = 'SIDE_NONE', 
                    sled = 2, ),
                protocol = 'SAS',
                raw_size_mi_b = 1831420,
                read_errors = dscc.models.error_count.ErrorCount(
                    correctable = 0, 
                    uncorrectable = 0, ),
                request_uri = '/v1/storage-systems/device-type1/7CE751P312/enclosures/9c3c4f29a82fd8d632ff379116fa0b8f/disks/d4b13e70924d29afdb77d932f7563ea6',
                resource_uri = '/v1/storage-systems/device-type1/7CE751P312/enclosures/0/disks/d4b13e70924d29afdb77d932f7563ea6',
                sed_status = 'FIPS Capable',
                speed = -1,
                state = dscc.models.state.State(
                    detailed = [
                        ''
                        ], 
                    overall = 'STATE_NORMAL', ),
                system_id = '7CE751P312',
                temp_max = 35,
                temp_min = 31,
                temp_now = 34,
                type = 'string',
                write_errors = dscc.models.error_count.ErrorCount(
                    correctable = 0, 
                    uncorrectable = 0, ),
                wwn = '5002538B10249591'
            )
        else:
            return DiskDetails(
        )
        """

    def testDiskDetails(self):
        """Test DiskDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
