# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_space_domain_fields_without_sort_key import NimbleSpaceDomainFieldsWithoutSortKey

class TestNimbleSpaceDomainFieldsWithoutSortKey(unittest.TestCase):
    """NimbleSpaceDomainFieldsWithoutSortKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleSpaceDomainFieldsWithoutSortKey:
        """Test NimbleSpaceDomainFieldsWithoutSortKey
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleSpaceDomainFieldsWithoutSortKey`
        """
        model = NimbleSpaceDomainFieldsWithoutSortKey()
        if include_optional:
            return NimbleSpaceDomainFieldsWithoutSortKey(
                app_category_id = '360000000000000000000000000000000000000006',
                app_category_name = 'Virtual Server',
                block_size = 4096,
                clone_ratio = 1,
                compressed_usage_bytes = 878976,
                compression_ratio = 40.3879423328965,
                dedupe_ratio = 1,
                deduped = True,
                encrypted = False,
                id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                logical_dedupe_usage = 0,
                physical_dedupe_usage = 0,
                pool_id = '0a473102de2f5f39d8000000000000000000000001',
                pool_name = 'default',
                savings_clone = 0,
                savings_compression = 34621056,
                savings_dedupe = 0,
                snap_logical_usage = 0,
                uncompressed_usage_bytes = 35500032,
                usage = 878976,
                vol_logical_usage = 35500032,
                vol_mapped_usage = 35500032
            )
        else:
            return NimbleSpaceDomainFieldsWithoutSortKey(
        )
        """

    def testNimbleSpaceDomainFieldsWithoutSortKey(self):
        """Test NimbleSpaceDomainFieldsWithoutSortKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
