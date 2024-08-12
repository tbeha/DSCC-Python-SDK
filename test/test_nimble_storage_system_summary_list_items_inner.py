# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_storage_system_summary_list_items_inner import NimbleStorageSystemSummaryListItemsInner

class TestNimbleStorageSystemSummaryListItemsInner(unittest.TestCase):
    """NimbleStorageSystemSummaryListItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleStorageSystemSummaryListItemsInner:
        """Test NimbleStorageSystemSummaryListItemsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleStorageSystemSummaryListItemsInner`
        """
        model = NimbleStorageSystemSummaryListItemsInner()
        if include_optional:
            return NimbleStorageSystemSummaryListItemsInner(
                id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                name = 'g1a1',
                access_protocol_list = [
                    'iscsi'
                    ],
                alarms_enabled = True,
                alert_from_email_addr = 'bob@example.com',
                alert_min_level = 'critical',
                alert_to_email_addrs = 'john-doe@example.com',
                allow_support_tunnel = False,
                array_unassign_migration_status = [
                    dscc.models.array_unassign_mig_status.ArrayUnassignMigStatus(
                        bytes_migrated = 56, 
                        bytes_remaining = 56, 
                        destination_arrays = [
                            dscc.models.nimble_arr_summary.NimbleArrSummary(
                                array_id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                                array_name = 'Array1', 
                                id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                                name = 'Array1', )
                            ], 
                        estimated_completion_time = 56, 
                        id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                        name = 'Array052', 
                        start_time = 56, )
                    ],
                arrays = dscc.models.nimble_array_list.NimbleArrayList(
                    items = [
                        dscc.models.nimble_array.NimbleArray(
                            all_flash = False, 
                            allow_lower_limits = True, 
                            available_bytes = 1234, 
                            create_pool = True, 
                            creation_time = 3400, 
                            ctrlr_a_support_ip = '128.0.0.1', 
                            ctrlr_b_support_ip = '128.0.0.1', 
                            customer_id = 'string', 
                            dedupe_capacity_bytes = 1234, 
                            dedupe_usage_bytes = 1234, 
                            extended_model = 'myobject-5', 
                            fc_port_count = 1234, 
                            force = False, 
                            full_name = 'myobject-5', 
                            generation = 0, 
                            gig_nic_port_count = 1234, 
                            group_state = 'initialized', 
                            id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                            is_fully_dedupe_capable = False, 
                            is_sfa = False, 
                            is_supported_hw_config = True, 
                            last_modified = 3400, 
                            model = 'myobject-5', 
                            model_sub_type = 'VMWare', 
                            name = 'NimbleArray', 
                            nic_list = [
                                dscc.models.nic_details.NICDetails(
                                    data_ip = '128.0.0.1', 
                                    name = 'NICName', 
                                    subnet_label = '255.255.255.0', 
                                    tagged = True, )
                                ], 
                            pending_delete_bytes = 1234, 
                            pool_description = '99.9999% availability', 
                            pool_id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                            pool_name = 'myobject-5', 
                            public_key = dscc.models.public_key_details.PublicKeyDetails(
                                key = 'DAQABAAABAQDR7pnlz5kehtrqNT9jIDP3KEVZdrYG64DH0ogJwLBM5fF27n/kssZt/NgcstPa2VvE6QTJQqW+3', 
                                key_name = 'root@abc', 
                                key_type = 'rsa', ), 
                            raw_capacity_bytes = 1234, 
                            resource_uri = '/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817', 
                            role = 'leader', 
                            search_name = 'vol:1', 
                            secondary_mgmt_ip = '128.0.0.1', 
                            serial = 'AC-109084', 
                            snap_compression = 9.18, 
                            snap_saved_bytes = 1234, 
                            snap_space_reduction = 9.18, 
                            snap_usage_bytes = 1234, 
                            snap_usage_uncompressed_bytes = 1234, 
                            status = 'reachable', 
                            ten_gig_sfp_nic_port_count = 1234, 
                            ten_gig_t_nic_port_count = 1234, 
                            upgrade = dscc.models.upgrade_details.UpgradeDetails(
                                messages = [
                                    dscc.models.nimble_error_with_arguments.NimbleErrorWithArguments(
                                        code = 13, 
                                        severity = 'info', 
                                        text = 'Error occurred.', )
                                    ], 
                                stage = 'finish', 
                                state = 'in_progress', 
                                type = 'offline', ), 
                            usable_cache_capacity_bytes = 1234, 
                            usable_capacity_bytes = 1234, 
                            usage = 1234, 
                            usage_valid = True, 
                            version = 'myobject-5', 
                            vol_compression = 9.18, 
                            vol_saved_bytes = 1234, 
                            vol_usage_bytes = 1234, 
                            vol_usage_uncompressed_bytes = 1234, 
                            zconf_ipaddrs = [
                                dscc.models.z_conf_i_paddrs.ZConfIPaddrs(
                                    ip_addr = '128.0.0.1', )
                                ], )
                        ], 
                    page_limit = 1, 
                    page_offset = 1, 
                    total = 1, ),
                associated_links = [{resourceUri=/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817/controllers/010df0fe6f7dc7bb16000000000000000000000007, type=controllers}],
                auto_switchover_enabled = True,
                auto_switchover_messages = [
                    dscc.models.nimble_error_with_arguments.NimbleErrorWithArguments(
                        code = 13, 
                        severity = 'info', 
                        text = 'Error occurred.', )
                    ],
                autoclean_unmanaged_snapshots_enabled = False,
                autoclean_unmanaged_snapshots_ttl_unit = 0,
                autosupport_enabled = True,
                cc_mode_enabled = False,
                clone_ratio = 9.18,
                cloud_management = 'read_only',
                common_resource_attributes = dscc.models.nimble_common_resource_attributes.NimbleCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                compressed_snap_usage_bytes = 0,
                compressed_vol_usage_bytes = 0,
                compression_ratio = 9.18,
                customer_id = 'string',
                data_rebalance_status = [
                    dscc.models.pool_rebalance_mig_status.PoolRebalanceMigStatus(
                        array_data_migration_status = [
                            dscc.models.array_mig_status.ArrayMigStatus(
                                id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                                is_data_source = True, 
                                name = 'Array056', 
                                space_utilization = 56, )
                            ], 
                        id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                        name = 'Pool3', 
                        pool_avg_space_utilization = 56, )
                    ],
                data_reduction_ratio = 9.18,
                var_date = 1598267193,
                dedupe_ratio = 9.18,
                default_iscsi_target_scope = 'group',
                default_snap_limit_percent = -1,
                default_snap_reserve = 0,
                default_snap_warn_level = 0,
                default_volume_limit = 100,
                default_volume_reserve = 0,
                default_volume_warn_level = 80,
                dns_servers = [
                    dscc.models.ip_address_object.IPAddressObject(
                        ip_addr = '10.0.0.11', )
                    ],
                domain_name = 'example-1.com',
                encryption_config = dscc.models.encryption_settings.EncryptionSettings(
                    cipher = 'none', 
                    encryption_active = True, 
                    encryption_key_manager = 'local', 
                    master_key_set = True, 
                    mode = 'none', 
                    scope = 'none', ),
                failover_mode = 'Manual',
                fc_enabled = False,
                free_space = 244695092429,
                generation = 0,
                group_snapshot_ttl = 0,
                group_target_enabled = True,
                group_target_name = 'iqn.2007-11.com.abc:g1a1-g00000000000004d3',
                iscsi_automatic_connection_method = False,
                iscsi_connection_rebalancing = False,
                iscsi_enabled = True,
                isns_enabled = True,
                isns_port = 3205,
                isns_server = 'example-1.com',
                last_login = 'admin @ 2020-08-06T17:26:01-0700',
                leader_array_name = 'arr1',
                leader_array_serial = 'AC-109084',
                management_service_backup_array_name = 'nimbleArray',
                management_service_backup_status = 'setup_in_progress',
                max_lock_period = 1209600,
                member_list = [
                    'nimbleArray'
                    ],
                merge_group_name = 'g1a2',
                merge_state = 'none',
                ntp_server = '0.abc.pool.ntp.org',
                num_connections = 0,
                num_snapcolls = 0,
                num_snaps = 0,
                pending_deletes = 0,
                proxy_port = 1234,
                proxy_server = 'example-1.com',
                proxy_username = 'usr1',
                raw_cache_capacity = 17179869184,
                raw_capacity = 476741369856,
                repl_throttle_list = [
                    dscc.models.throttle.Throttle(
                        creation_time = 56, 
                        days = 'example day', 
                        description = 'Throttle one', 
                        id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                        last_modified = 56, 
                        name = 'Throttle1', 
                        thr_at_time = 10800, 
                        thr_bandwidth = 14, 
                        thr_bandwidth_kbps = 1400, 
                        thr_bandwidth_limit_kbps = 1400, 
                        thr_day_mask = 41, 
                        thr_partner_id = '001d9973433673c3db000000000000000000000001', 
                        thr_until_time = 14400, )
                    ],
                repl_throttled_bandwidth = -1,
                repl_throttled_bandwidth_kbps = -1,
                resource_uri = '/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817',
                savings = 1073741824,
                savings_clone = 0,
                savings_compression = 0,
                savings_data_reduction = 0,
                savings_dedupe = 0,
                savings_ratio = 9.18,
                savings_vol_thin_provisioning = 1073741824,
                scsi_vendor_id = 'Nimble',
                send_alert_to_support = True,
                smtp_port = 25,
                smtp_server = '',
                snap_compression_ratio = 9.18,
                snap_retn_meter_high = 0,
                snap_retn_meter_very_high = 0,
                snap_usage_populated = 0,
                snmp_community = 'public',
                snmp_get_enabled = False,
                snmp_get_port = 161,
                snmp_sys_contact = 'JD',
                snmp_sys_location = 'example-location',
                snmp_trap_enabled = True,
                snmp_trap_host = 'example-1.com',
                snmp_trap_port = 162,
                space_info_valid = False,
                syslogd_enabled = True,
                syslogd_port = 514,
                syslogd_server = 'example-1.com',
                syslogd_servers = [
                    dscc.models.nimble_syslogd_server_info.NimbleSyslogdServerInfo(
                        syslog_port = 1080, 
                        syslog_server = 'sysloghost-1.com', )
                    ],
                system_headroom = dscc.models.system_headroom.systemHeadroom(
                    performance = dscc.models.performance_headroom.performanceHeadroom(
                        available_headroom = 'Low', 
                        headroom_utilization = 'Low', 
                        utilization = 10, ), ),
                tdz_enabled = False,
                tdz_prefix = 'peerzone',
                timezone = 'America/Los_Angeles',
                tlsv1_enabled = False,
                uncompressed_snap_usage_bytes = 0,
                uncompressed_vol_usage_bytes = 0,
                unique_name_enabled = False,
                unused_reserve_bytes = 0,
                update_array_names = 'name,app_id',
                update_download_end_time = 1460477575,
                update_download_error_code = 'SM_ok',
                update_download_start_time = 1460477565,
                update_downloading = False,
                update_end_time = 3400,
                update_error_code = 'SM_ok',
                update_progress_msg = 'example progress message',
                update_start_time = 3400,
                update_state = 'normal',
                usable_cache_capacity = 13432258560,
                usable_capacity_bytes = 244695092429,
                usage = 0,
                usage_valid = True,
                user_inactivity_timeout = 1800,
                version_current = '5.3.0.0-746508-opt',
                version_rollback = 'v1',
                version_target = 'v1',
                vol_compression_ratio = 9.18,
                vol_thin_provisioning_ratio = 9.18,
                volume_migration_status = [
                    dscc.models.vol_fam_mig_status.VolFamMigStatus(
                        array_list = [
                            dscc.models.array_mig_status.ArrayMigStatus(
                                id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                                is_data_source = True, 
                                name = 'Array056', 
                                space_utilization = 56, )
                            ], 
                        dest_pool_id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                        dest_pool_name = 'Pool2', 
                        move_bytes_migrated = 56, 
                        move_bytes_remaining = 56, 
                        move_est_compl_time = 56, 
                        move_start_time = 56, 
                        root_vol_id = '', 
                        root_vol_name = 'Root volume', 
                        source_pool_id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                        source_pool_name = 'Pool1', )
                    ],
                vss_validation_timeout = 60,
                vvol_enabled = True,
                witness_status = [
                    dscc.models.witness_test_response.WitnessTestResponse(
                        array_name = 'Nimble Array056', 
                        role = 'leader', 
                        witness_connectivity_message = 'example reachability message', 
                        witness_connectivity_state = 'reachable', )
                    ]
            )
        else:
            return NimbleStorageSystemSummaryListItemsInner(
        )
        """

    def testNimbleStorageSystemSummaryListItemsInner(self):
        """Test NimbleStorageSystemSummaryListItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
