# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.create_bulk_merge_candidates_object import CreateBulkMergeCandidatesObject

class TestCreateBulkMergeCandidatesObject(unittest.TestCase):
    """CreateBulkMergeCandidatesObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateBulkMergeCandidatesObject:
        """Test CreateBulkMergeCandidatesObject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateBulkMergeCandidatesObject`
        """
        model = CreateBulkMergeCandidatesObject()
        if include_optional:
            return CreateBulkMergeCandidatesObject(
                duplicate_ids = [
                    ''
                    ],
                members = [
                    ''
                    ],
                name = 'host1',
                systems = [
                    ''
                    ]
            )
        else:
            return CreateBulkMergeCandidatesObject(
                duplicate_ids = [
                    ''
                    ],
                members = [
                    ''
                    ],
                name = 'host1',
                systems = [
                    ''
                    ],
        )
        """

    def testCreateBulkMergeCandidatesObject(self):
        """Test CreateBulkMergeCandidatesObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
