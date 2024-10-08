# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_v_collection_details import NimbleVCollectionDetails

class TestNimbleVCollectionDetails(unittest.TestCase):
    """NimbleVCollectionDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleVCollectionDetails:
        """Test NimbleVCollectionDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleVCollectionDetails`
        """
        model = NimbleVCollectionDetails()
        if include_optional:
            return NimbleVCollectionDetails(
                agent_hostname = 'myobject-5',
                app_sync = 'vss',
                associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817","type":"storage-systems"}],
                cache_pinned_volume_list = [
                    dscc.models.nimble_volume_summary.NimbleVolumeSummary(
                        agent_type = 'vvol', 
                        has_locked_snapshots = False, 
                        id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                        name = 'Volume0', 
                        vol_id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                        vol_name = 'Volume0', 
                        volume_creator_id = '0600000000000004d3000000000044000000000002', 
                        volume_creator_name = 'AF-1234567', )
                    ],
                common_resource_attributes = dscc.models.nimble_common_resource_attributes.NimbleCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'data-ops-manager/storage-systems/device-type2/001491cb6652a03a6b000000000000000000000001/volume-collections/071491cb6652a03a6b000000000000000000000006',
                creation_time = 1599110308,
                customer_id = 'string',
                description = '99.9999% availability',
                downstream_volume_list = [
                    dscc.models.nimble_volume_collection_volume_pool_info.NimbleVolumeCollectionVolumePoolInfo(
                        pool_id = '0a1c9973433673c3db000000000000000000000001', 
                        pool_name = 'default', 
                        vol_id = '061c9973433673c3db000000000000000000000001', 
                        vol_name = 'vol', 
                        volume_creator_id = '0600000000000004d3000000000044000000000002', 
                        volume_creator_name = 'AF-1234567', )
                    ],
                full_name = 'vol',
                generation = 0,
                handover_replication_partner = 'myobject-5',
                is_handing_over = False,
                is_mfa_protected = True,
                is_standalone_volcoll = False,
                lag_time = 3400,
                last_replicated_snapcoll = dscc.models.nimble_snapcoll_summary.NimbleSnapcollSummary(
                    snapcoll_creation_time = '1601481600', 
                    snapcoll_id = '051c9973433673c3db00000000000000000000001c', 
                    snapcoll_name = 'vol-daily-2020-10-01::00:00:00.000', ),
                last_snapcoll = dscc.models.nimble_snapcoll_summary.NimbleSnapcollSummary(
                    snapcoll_creation_time = '1601481600', 
                    snapcoll_id = '051c9973433673c3db00000000000000000000001c', 
                    snapcoll_name = 'vol-daily-2020-10-01::00:00:00.000', ),
                metadata = [
                    dscc.models.nimble_ns_key_value.NimbleNsKeyValue(
                        key = 'name', 
                        value = 'AA-100373', )
                    ],
                pol_owner_name = 'system1',
                protection_type = 'local',
                repl_bytes_transferred = 1234,
                repl_priority = 'high',
                replication_partner = [
                    ''
                    ],
                resource_uri = '/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817',
                schedule_list = [
                    dscc.models.nimble_ns_schedule.NimbleNsSchedule(
                        active = False, 
                        at_time = 0, 
                        days = 'all', 
                        disable_appsync = True, 
                        downstream_partner = 'abc', 
                        downstream_partner_id = '0c1c9973433673c3db000000000000000000000008', 
                        downstream_partner_name = 'abc', 
                        id = '0c1c9973433673c3db000000000000000000000008', 
                        mfa_protected = True, 
                        name = 'daily', 
                        num_retain = 30, 
                        num_retain_replica = 0, 
                        period = 1, 
                        period_unit = 'days', 
                        repl_alert_thres = 86400, 
                        replicate_every = 0, 
                        schedule_id = '0c1c9973433673c3db000000000000000000000008', 
                        schedule_name = 'daily', 
                        schedule_type = 'regular', 
                        skip_db_consistency_check = False, 
                        snap_verify = True, 
                        until_time = 86399, )
                    ],
                search_name = 'vol',
                snapcoll_count = 1,
                srep_last_sync = 0,
                srep_resync_percent = 10,
                total_repl_bytes = 1234,
                type = 'string',
                upstream_volume_list = [
                    dscc.models.nimble_volume_collection_volume_pool_info.NimbleVolumeCollectionVolumePoolInfo(
                        pool_id = '0a1c9973433673c3db000000000000000000000001', 
                        pool_name = 'default', 
                        vol_id = '061c9973433673c3db000000000000000000000001', 
                        vol_name = 'vol', 
                        volume_creator_id = '0600000000000004d3000000000044000000000002', 
                        volume_creator_name = 'AF-1234567', )
                    ],
                vcenter_hostname = 'myobject-5',
                vcenter_username = 'administrator@vsphere.local',
                volcoll_creator_id = '0600000000000004d3000000000044000000000002',
                volcoll_creator_name = 'AF-123456',
                volume_count = 1,
                volume_list = [
                    dscc.models.nimble_volume_summary.NimbleVolumeSummary(
                        agent_type = 'vvol', 
                        has_locked_snapshots = False, 
                        id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                        name = 'Volume0', 
                        vol_id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                        vol_name = 'Volume0', 
                        volume_creator_id = '0600000000000004d3000000000044000000000002', 
                        volume_creator_name = 'AF-1234567', )
                    ]
            )
        else:
            return NimbleVCollectionDetails(
        )
        """

    def testNimbleVCollectionDetails(self):
        """Test NimbleVCollectionDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
