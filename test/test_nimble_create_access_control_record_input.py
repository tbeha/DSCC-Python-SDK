# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_create_access_control_record_input import NimbleCreateAccessControlRecordInput

class TestNimbleCreateAccessControlRecordInput(unittest.TestCase):
    """NimbleCreateAccessControlRecordInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleCreateAccessControlRecordInput:
        """Test NimbleCreateAccessControlRecordInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleCreateAccessControlRecordInput`
        """
        model = NimbleCreateAccessControlRecordInput()
        if include_optional:
            return NimbleCreateAccessControlRecordInput(
                apply_to = 'pe',
                chap_user_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                initiator_group_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                lun = 8,
                pe_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                pe_ids = [
                    '2a0df0fe6f7dc7bb16000000000000000000004817'
                    ],
                snap_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                system_uid = '2a0df0fe6f7dc7bb16000000000000000000004817',
                vol_id = '064323bdd90b39c3a7000000000000000000000016'
            )
        else:
            return NimbleCreateAccessControlRecordInput(
        )
        """

    def testNimbleCreateAccessControlRecordInput(self):
        """Test NimbleCreateAccessControlRecordInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
