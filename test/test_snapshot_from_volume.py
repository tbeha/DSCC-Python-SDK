# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.snapshot_from_volume import SnapshotFromVolume

class TestSnapshotFromVolume(unittest.TestCase):
    """SnapshotFromVolume unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnapshotFromVolume:
        """Test SnapshotFromVolume
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SnapshotFromVolume`
        """
        model = SnapshotFromVolume()
        if include_optional:
            return SnapshotFromVolume(
                id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                name = 'snap1',
                snap_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                snap_name = 'snap1'
            )
        else:
            return SnapshotFromVolume(
        )
        """

    def testSnapshotFromVolume(self):
        """Test SnapshotFromVolume"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
