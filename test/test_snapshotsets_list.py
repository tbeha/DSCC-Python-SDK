# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.snapshotsets_list import SnapshotsetsList

class TestSnapshotsetsList(unittest.TestCase):
    """SnapshotsetsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnapshotsetsList:
        """Test SnapshotsetsList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SnapshotsetsList`
        """
        model = SnapshotsetsList()
        if include_optional:
            return SnapshotsetsList(
                app_set_business_unit = 'cssl',
                app_set_comments = 'app set comments',
                app_set_exclude_aiqo_s = 'no',
                app_set_importance = 'MEDIUM',
                app_set_name = 'KA_VEGA_APPSET1_186',
                app_set_type = 'Oracle Database',
                comment = 'Comments',
                common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                creation_time = dscc.models.device_type4_snapshotset_list_single_creation_time.DeviceType4SnapshotsetListSingle_creationTime(
                    ms = 56, 
                    tz = '', ),
                customer_id = 'string',
                display_name = 'Application Set KA_VEGA_APPSET1_186 ',
                domain = 'Domain',
                export_status = 'PARTIALLY_EXPORTED',
                generation = 0,
                id = '4c74ec5c-ecec-4483-9506-3fb5dc45b5d0',
                kv_pairs_present = True,
                members = ["vol1","vol2"],
                name = 'KA_VEGA_APPSET2_186',
                request_uri = '/v1/storage-systems/device-type1/7CE751P312/applicationsets/fd3244ef7f1ab8bd16500c7a41bdf8f8/snapshots',
                serial_number = '7CE738P06J',
                snap_set_id = 5,
                snap_set_parent_id = 5,
                snap_set_parent_name = 'HPE',
                system_id = '7CE751P312',
                type = 'string',
                vv_set_type = 'VVSET'
            )
        else:
            return SnapshotsetsList(
        )
        """

    def testSnapshotsetsList(self):
        """Test SnapshotsetsList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
