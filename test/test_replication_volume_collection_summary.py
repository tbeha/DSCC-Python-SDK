# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.replication_volume_collection_summary import ReplicationVolumeCollectionSummary

class TestReplicationVolumeCollectionSummary(unittest.TestCase):
    """ReplicationVolumeCollectionSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReplicationVolumeCollectionSummary:
        """Test ReplicationVolumeCollectionSummary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReplicationVolumeCollectionSummary`
        """
        model = ReplicationVolumeCollectionSummary()
        if include_optional:
            return ReplicationVolumeCollectionSummary(
                id = '07717d935c0fa5075d000000000000000000000008'
            )
        else:
            return ReplicationVolumeCollectionSummary(
        )
        """

    def testReplicationVolumeCollectionSummary(self):
        """Test ReplicationVolumeCollectionSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
