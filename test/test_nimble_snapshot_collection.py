# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_snapshot_collection import NimbleSnapshotCollection

class TestNimbleSnapshotCollection(unittest.TestCase):
    """NimbleSnapshotCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleSnapshotCollection:
        """Test NimbleSnapshotCollection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleSnapshotCollection`
        """
        model = NimbleSnapshotCollection()
        if include_optional:
            return NimbleSnapshotCollection(
                has_locked_snapshots = True,
                id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                name = 'snap1',
                online_status = 'online',
                schedule_id = '2a1df0fe6f7dc7bb16000000000000000000004017',
                srep_owner_id = '2a1df0fe6f7dc7bb16000000000000000000004017',
                volcoll_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                allow_writes = False,
                associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817","type":"storage-systems"}],
                common_resource_attributes = dscc.models.nimble_common_resource_attributes.NimbleCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'null',
                creation_time = 1598951404,
                customer_id = 'string',
                description = '99.9999% availability',
                generation = 0,
                is_complete = False,
                is_external_trigger = False,
                is_manual = False,
                is_manually_managed = False,
                is_mfa_protected = True,
                is_replica = False,
                is_unmanaged = True,
                last_modified = 1598952427,
                metadata = [
                    dscc.models.key_value.KeyValue(
                        key = 'key1', 
                        value = 'value1', )
                    ],
                origin_name = 'myobject-5',
                peer_snapcoll_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                repl_status = 'in_progress',
                replicate_to = 'myobject-5',
                resource_uri = '/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817',
                snapshots_list = [
                    dscc.models.nimble_snap_coll_snapshot.NimbleSnapCollSnapshot(
                        expiry_time = 0, 
                        id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                        name = 'snap1', 
                        schedule_id = '0c40f75f5b73693a47000000000000000000000018', 
                        schedule_name = 'Schedule-new', 
                        snap_collection_id = '2a0df0fe6f7dc7bb16000000000000000000004014', 
                        snap_collection_name = 'snp1', 
                        vol_id = '0625dab4ed8948f2e000000000000000000000003a', 
                        vol_name = 'vol1', 
                        volume_creator_id = '0600000000000004d3000000000044000000000002', 
                        volume_creator_name = 'AF-123456', )
                    ],
                type = 'string',
                volcoll_creator_id = '0600000000000004d3000000000044000000000002',
                volcoll_creator_name = 'AF-123456'
            )
        else:
            return NimbleSnapshotCollection(
        )
        """

    def testNimbleSnapshotCollection(self):
        """Test NimbleSnapshotCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
