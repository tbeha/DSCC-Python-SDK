# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.create_bulk_merge_candidates import CreateBulkMergeCandidates

class TestCreateBulkMergeCandidates(unittest.TestCase):
    """CreateBulkMergeCandidates unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateBulkMergeCandidates:
        """Test CreateBulkMergeCandidates
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateBulkMergeCandidates`
        """
        model = CreateBulkMergeCandidates()
        if include_optional:
            return CreateBulkMergeCandidates(
                items = [
                    dscc.models.create_bulk_merge_candidates_object.CreateBulkMergeCandidatesObject(
                        duplicate_ids = [
                            ''
                            ], 
                        members = [
                            ''
                            ], 
                        name = 'host1', 
                        systems = [
                            ''
                            ], )
                    ]
            )
        else:
            return CreateBulkMergeCandidates(
        )
        """

    def testCreateBulkMergeCandidates(self):
        """Test CreateBulkMergeCandidates"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
