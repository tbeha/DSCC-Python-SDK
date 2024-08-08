# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4disks_list import DeviceType4disksList

class TestDeviceType4disksList(unittest.TestCase):
    """DeviceType4disksList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4disksList:
        """Test DeviceType4disksList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4disksList`
        """
        model = DeviceType4disksList()
        if include_optional:
            return DeviceType4disksList(
                admit_time = dscc.models.device_type4_admit_time.DeviceType4AdmitTime(
                    ms = 1591599192000, 
                    tz = 'Asia/Calcutta', ),
                associated_links = [{"resourceUri":"/v1/storage-systems/device-type4/7CE751P312","type":"systems"},{"resourceUri":"/v1/storage-systems/device-type4/7CE751P312/enclosures/0","type":"enclosures"}],
                capacity = dscc.models.device_type4filter_disk_capacity.DeviceType4filterDiskCapacity(
                    allocated_mi_b = 595968, 
                    failed_mi_b = 0, 
                    free_mi_b = 1233920, 
                    total_mi_b = 595968, 
                    unavailable_mi_b = 0, ),
                common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                consumable_size_mi_b = 1829888,
                customer_id = 'string',
                dev_type = 'DEVTYPE_SSD',
                disk_id = 1,
                displayname = 'Drive 0.SIDE_NONE.2.0',
                domain = '',
                enclosure_uid = '9c3c4f29a82fd8d632ff379116fa0b8f',
                fw_status = '--',
                fw_version = '3P00',
                generation = 0,
                id = 'd4b13e70924d29afdb77d932f7563ea6',
                insert_time = dscc.models.device_type4_admit_time.DeviceType4AdmitTime(
                    ms = 1591599192000, 
                    tz = 'Asia/Calcutta', ),
                life_left_pct = 100,
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
                media_type = 'MLC',
                mfg_capacity_gb = 1920,
                paths = [
                    dscc.models.device_type4_disk_loop_inner.DeviceType4DiskLoop_inner(
                        degraded = False, 
                        disabled = False, 
                        port = dscc.models.device_type4_disk_port_position.DeviceType4DiskPortPosition(
                            node = 0, 
                            slot = 0, ), 
                        primary = False, )
                    ],
                position_last = dscc.models.device_type4_disk_position.DeviceType4DiskPosition(
                    cage = 0, 
                    sled = 2, ),
                position_now = dscc.models.device_type4filter_disk_position_now.DeviceType4filterDiskPositionNow(
                    cage = 0, 
                    sled = 2, ),
                protocol = 'SAS',
                raw_size_mi_b = 1831420,
                read_errors = dscc.models.device_type4_error_count.DeviceType4ErrorCount(
                    correctable = 0, 
                    uncorrectable = 0, ),
                resource_uri = '/v1/storage-systems/device-type4/7CE751P312/enclosures/0/disks/d4b13e70924d29afdb77d932f7563ea6',
                sed_status = 'FIPS Capable',
                state = dscc.models.device_type4_state.DeviceType4State(
                    detailed = [
                        ''
                        ], 
                    overall = 'STATE_NORMAL', ),
                system_id = '7CE751P312',
                type = 'string',
                write_errors = dscc.models.device_type4_error_count.DeviceType4ErrorCount(
                    correctable = 0, 
                    uncorrectable = 0, ),
                wwn = '5002538B10249591'
            )
        else:
            return DeviceType4disksList(
        )
        """

    def testDeviceType4disksList(self):
        """Test DeviceType4disksList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
