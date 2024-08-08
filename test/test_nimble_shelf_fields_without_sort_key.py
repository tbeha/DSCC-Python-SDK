# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_shelf_fields_without_sort_key import NimbleShelfFieldsWithoutSortKey

class TestNimbleShelfFieldsWithoutSortKey(unittest.TestCase):
    """NimbleShelfFieldsWithoutSortKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleShelfFieldsWithoutSortKey:
        """Test NimbleShelfFieldsWithoutSortKey
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleShelfFieldsWithoutSortKey`
        """
        model = NimbleShelfFieldsWithoutSortKey()
        if include_optional:
            return NimbleShelfFieldsWithoutSortKey(
                array_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                array_name = 'myobject-5',
                id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                model = 'CS210',
                serial = 'AA-100373'
            )
        else:
            return NimbleShelfFieldsWithoutSortKey(
        )
        """

    def testNimbleShelfFieldsWithoutSortKey(self):
        """Test NimbleShelfFieldsWithoutSortKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
