# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_edit_multiple_snapshot_input import NimbleEditMultipleSnapshotInput

class TestNimbleEditMultipleSnapshotInput(unittest.TestCase):
    """NimbleEditMultipleSnapshotInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleEditMultipleSnapshotInput:
        """Test NimbleEditMultipleSnapshotInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleEditMultipleSnapshotInput`
        """
        model = NimbleEditMultipleSnapshotInput()
        if include_optional:
            return NimbleEditMultipleSnapshotInput(
                snapshot_list = [
                    dscc.models.nimble_edit_snapshot_input.NimbleEditSnapshotInput(
                        app_uuid = 'rfc4122.943f7dc1-5853-497c-b530-f689ccf1bf18', 
                        description = '99.9999% availability', 
                        id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                        lock_period = 0, 
                        metadata = [
                            dscc.models.key_value.KeyValue(
                                key = 'key1', 
                                value = 'value1', )
                            ], 
                        online = False, )
                    ]
            )
        else:
            return NimbleEditMultipleSnapshotInput(
                snapshot_list = [
                    dscc.models.nimble_edit_snapshot_input.NimbleEditSnapshotInput(
                        app_uuid = 'rfc4122.943f7dc1-5853-497c-b530-f689ccf1bf18', 
                        description = '99.9999% availability', 
                        id = '2a0df0fe6f7dc7bb16000000000000000000004817', 
                        lock_period = 0, 
                        metadata = [
                            dscc.models.key_value.KeyValue(
                                key = 'key1', 
                                value = 'value1', )
                            ], 
                        online = False, )
                    ],
        )
        """

    def testNimbleEditMultipleSnapshotInput(self):
        """Test NimbleEditMultipleSnapshotInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
