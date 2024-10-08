# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_volume_filterable_fields import NimbleVolumeFilterableFields

class TestNimbleVolumeFilterableFields(unittest.TestCase):
    """NimbleVolumeFilterableFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleVolumeFilterableFields:
        """Test NimbleVolumeFilterableFields
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleVolumeFilterableFields`
        """
        model = NimbleVolumeFilterableFields()
        if include_optional:
            return NimbleVolumeFilterableFields(
                base_snap_id = '2a0df0fe6f7dc7bb16000000000000000000004017',
                base_snap_name = 'snp1',
                clone = False,
                dest_pool_id = '0a00000000000004d3000000000000000000000001',
                dest_pool_name = 'myobject-5',
                folder_id = '1234123412341234123412341234123412341234cd',
                folder_name = 'myobject-5',
                id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                name = 'volume1',
                online = True,
                owned_by_group = 'g1a1',
                owned_by_group_id = '2a0df0fe6f7dc7bb16000000000000000000004007',
                parent_vol_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                parent_vol_name = '1234123412341234abcdacbdacbdacbd',
                perfpolicy_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                perfpolicy_name = 'default',
                pool_id = '0a00000000000004d3000000000000000000000001',
                pool_name = 'default',
                read_only = False,
                replication_role = 'no_replication',
                secondary_serial_number = '1234123412341234abcdacbdacbdacbd',
                serial_number = '5596fd1da1c87b8d6c9ce900d3040000',
                size = 1024,
                target_name = 'iqn.2007-11.com.storage:vol0.762157726640911-v00000000000004d3.00000005.000004d3',
                volcoll_id = '1234123412341234123412341234123412341234cd',
                volcoll_name = 'myobject-5'
            )
        else:
            return NimbleVolumeFilterableFields(
        )
        """

    def testNimbleVolumeFilterableFields(self):
        """Test NimbleVolumeFilterableFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
