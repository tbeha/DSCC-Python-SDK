# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_volume_collection_volume_pool_info import NimbleVolumeCollectionVolumePoolInfo

class TestNimbleVolumeCollectionVolumePoolInfo(unittest.TestCase):
    """NimbleVolumeCollectionVolumePoolInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleVolumeCollectionVolumePoolInfo:
        """Test NimbleVolumeCollectionVolumePoolInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleVolumeCollectionVolumePoolInfo`
        """
        model = NimbleVolumeCollectionVolumePoolInfo()
        if include_optional:
            return NimbleVolumeCollectionVolumePoolInfo(
                pool_id = '0a1c9973433673c3db000000000000000000000001',
                pool_name = 'default',
                vol_id = '061c9973433673c3db000000000000000000000001',
                vol_name = 'vol',
                volume_creator_id = '0600000000000004d3000000000044000000000002',
                volume_creator_name = 'AF-1234567'
            )
        else:
            return NimbleVolumeCollectionVolumePoolInfo(
        )
        """

    def testNimbleVolumeCollectionVolumePoolInfo(self):
        """Test NimbleVolumeCollectionVolumePoolInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
