# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_create_folder_input import NimbleCreateFolderInput

class TestNimbleCreateFolderInput(unittest.TestCase):
    """NimbleCreateFolderInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleCreateFolderInput:
        """Test NimbleCreateFolderInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleCreateFolderInput`
        """
        model = NimbleCreateFolderInput()
        if include_optional:
            return NimbleCreateFolderInput(
                access_protocol = 'iscsi',
                agent_type = 'openstack',
                appserver_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                description = '99.9999% availability',
                host_initiator_group_ids = ["b58856f40db14f109186810b61bf72e9"],
                host_initiators_ids = ["7c021a70a50e4437a13bd08542a75667"],
                inherited_vol_perfpol_id = '030a259996ae869835000000000000000000000001',
                limit_iops = -1,
                limit_mbps = -1,
                limit_size_bytes = -1,
                name = 'myobject-5',
                overdraft_limit_pct = 0,
                pool_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                provisioned_limit_size_bytes = -1
            )
        else:
            return NimbleCreateFolderInput(
                name = 'myobject-5',
                pool_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
        )
        """

    def testNimbleCreateFolderInput(self):
        """Test NimbleCreateFolderInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
