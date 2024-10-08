# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_snapshots_summary_list import DeviceType4SnapshotsSummaryList

class TestDeviceType4SnapshotsSummaryList(unittest.TestCase):
    """DeviceType4SnapshotsSummaryList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4SnapshotsSummaryList:
        """Test DeviceType4SnapshotsSummaryList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4SnapshotsSummaryList`
        """
        model = DeviceType4SnapshotsSummaryList()
        if include_optional:
            return DeviceType4SnapshotsSummaryList(
                items = [
                    dscc.models.device_type4snapshots_list.DeviceType4snapshotsList(
                        admin_allocation_settings = dscc.models.device_type4user_allocation_settings_single.DeviceType4userAllocationSettingsSingle(
                            ha = dscc.models.deprecated_device_type4user_allocation_settings_single_ha.DeprecatedDeviceType4userAllocationSettingsSingle_HA(
                                default = 'Magazine', 
                                key = 'hajbod-10', ), 
                            raid_type = '', 
                            device_speed = dscc.models.device_type4device_speed_single.DeviceType4deviceSpeedSingle(
                                text = '', 
                                value = 56, ), 
                            device_type = '', 
                            disk_filter = '', 
                            requested_ha = dscc.models.deprecated_device_type4user_allocation_settings_single_ha.DeprecatedDeviceType4userAllocationSettingsSingle_HA(
                                default = 'Magazine', 
                                key = 'hajbod-10', ), 
                            set_size = '', 
                            step_size = 56, ), 
                        base_id = 56, 
                        comment = '', 
                        common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                            cloud_state = 'CONNECTED', ), 
                        compression_policy = '', 
                        conversion_type = 'CONVERSIONTYPE_THIN', 
                        copy_of_id = 56, 
                        creation_time = dscc.models.device_type4_snapshots_list_single_creation_time.DeviceType4SnapshotsListSingle_creationTime(
                            ms = 56, 
                            tz = '', ), 
                        customer_id = 'string', 
                        data_reduction = '', 
                        dedup = '', 
                        dev_type = '', 
                        displayname = '', 
                        domain = '', 
                        efficiency_update_time = dscc.models.deprecated_device_type4calendar.DeprecatedDeviceType4calendar(
                            ms = 56, 
                            tz = '', ), 
                        expiration_time = dscc.models.deprecated_device_type4calendar.DeprecatedDeviceType4calendar(
                            ms = 56, 
                            tz = '', ), 
                        fully_provisioned = True, 
                        generation = 0, 
                        heads_per_cylinder = 56, 
                        health_state = 56, 
                        hidden = True, 
                        id = 'b7107a30-260a-41c1-a47f-e50770c414c9', 
                        initiators = [
                            dscc.models.device_type4_application_set_details_initiators_inner.DeviceType4ApplicationSetDetails_initiators_inner(
                                device_discovered_name = 'TEST11', 
                                id = '6848ef683c27403e96caa51816ddc72c', 
                                resource_uri = '/v1/host-initiators/6848ef683c27403e96caa51816ddc72c', 
                                type = 'host-initiators', )
                            ], 
                        name = 'Finance', 
                        parent_id = 56, 
                        phys_parent_id = 56, 
                        physical_copy = True, 
                        policy = dscc.models.device_type4policy.DeviceType4policy(
                            file_service = True, 
                            host_dif3par = True, 
                            host_dif_std = True, 
                            no_cache = True, 
                            one_host = True, 
                            stale_snapshot = True, 
                            system = True, 
                            zero_detect = True, 
                            zero_fill = True, ), 
                        prov_type = '', 
                        raid = '', 
                        rcopy_status = '', 
                        read_only = True, 
                        retention_time = , 
                        ro_child_id = 56, 
                        rw_child_id = 56, 
                        sectors_per_track = 56, 
                        shared_parent_id = 56, 
                        snapshot_alloc_limit = 56, 
                        snapshot_alloc_warning = 56, 
                        snapshot_allocation_settings = dscc.models.deprecated_device_type4user_allocation_settings_single.DeprecatedDeviceType4userAllocationSettingsSingle(
                            raid_type = '', 
                            device_type = '', 
                            disk_filter = '', 
                            set_size = '', 
                            step_size = 56, ), 
                        snapshot_capacity = dscc.models.device_type4_snapshot_capacity.DeviceType4SnapshotCapacity(
                            admin_space = dscc.models.device_type4space.DeviceType4space(
                                free_mi_b = 1.337, 
                                grown_mi_b = 1.337, 
                                raw_reserved_mi_b = 1.337, 
                                reclaimed_mi_b = 1.337, 
                                reserved_mi_b = 1.337, 
                                total_mi_b = 1.337, 
                                used_mi_b = 1.337, ), 
                            branch_used_blocks_mi_b = 1.337, 
                            branch_v_size_mi_b = 2048, 
                            compact_efficiency = 1.337, 
                            compression_efficiency = 1.337, 
                            copied_mb = 1.337, 
                            copied_perc = 56, 
                            ddc_size = 1.337, 
                            dds_size = 1.337, 
                            dedup_savings_size = 1.337, 
                            dedup_written_size = 1.337, 
                            host_written_mi_b = 1.337, 
                            host_written_to_virtual_percent = 1.337, 
                            size_mi_b = 1.337, 
                            snapshot_tdvv_size = dscc.models.device_type4snapshot_tdvvsize.DeviceType4snapshotTdvvsize(
                                ddc_size_mi_b = 1.337, 
                                dds_size_mi_b = 1.337, 
                                virtual_size_mi_b = 1.337, 
                                written_size_mi_b = 1.337, ), 
                            snapshot_used_to_virtual_percent = 1.337, 
                            total_raw_reserved_mi_b = 1.337, 
                            total_reserved_mi_b = 1.337, 
                            total_space_mi_b = 1.337, 
                            used_blocks_mi_b = 1.337, 
                            used_capacity = 1.337, 
                            used_size_mi_b = 1.337, 
                            user_reserved_to_virtual_percent = 1.337, 
                            user_space = dscc.models.device_type4space.DeviceType4space(
                                free_mi_b = 1.337, 
                                grown_mi_b = 1.337, 
                                raw_reserved_mi_b = 1.337, 
                                reclaimed_mi_b = 1.337, 
                                reserved_mi_b = 1.337, 
                                total_mi_b = 1.337, 
                                used_mi_b = 1.337, ), 
                            user_used_to_virtual_percent = 1.337, ), 
                        snapshot_id = 56, 
                        snapshot_type = '', 
                        space_calculation_time = , 
                        started = True, 
                        state = dscc.models.device_type4_state.DeviceType4State(
                            detailed = [
                                ''
                                ], 
                            overall = 'STATE_NORMAL', ), 
                        system_id = '7CE751P312', 
                        thin_provisioned = True, 
                        type = 'string', 
                        unref_space_freed_time = , 
                        user_alloc_limit = 56, 
                        user_alloc_warning = 56, 
                        user_allocation_settings = dscc.models.device_type4user_allocation_settings_single.DeviceType4userAllocationSettingsSingle(
                            raid_type = '', 
                            device_type = '', 
                            disk_filter = '', 
                            set_size = '', 
                            step_size = 56, ), 
                        user_cpg_id = 56, 
                        user_cpg_name = '', 
                        vlun_sector_size = 56, 
                        wwn = '60002AC0000000000000006B0001FFEB', )
                    ],
                page_limit = 1,
                page_offset = 1,
                request_uri = '/v1/storage-systems/device-type4/7CE751P312/applicationsets/8c18425671d44803b4512f4ca1917410/snapshots',
                total = 1
            )
        else:
            return DeviceType4SnapshotsSummaryList(
        )
        """

    def testDeviceType4SnapshotsSummaryList(self):
        """Test DeviceType4SnapshotsSummaryList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
