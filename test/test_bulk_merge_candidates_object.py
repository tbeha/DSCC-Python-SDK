# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.bulk_merge_candidates_object import BulkMergeCandidatesObject

class TestBulkMergeCandidatesObject(unittest.TestCase):
    """BulkMergeCandidatesObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BulkMergeCandidatesObject:
        """Test BulkMergeCandidatesObject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BulkMergeCandidatesObject`
        """
        model = BulkMergeCandidatesObject()
        if include_optional:
            return BulkMergeCandidatesObject(
                duplicate_ids = [
                    ''
                    ],
                id = '6848ef683c27403e96caa51816ddc72c',
                members = [
                    ''
                    ],
                name = 'host1',
                systems = [
                    ''
                    ]
            )
        else:
            return BulkMergeCandidatesObject(
        )
        """

    def testBulkMergeCandidatesObject(self):
        """Test BulkMergeCandidatesObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
