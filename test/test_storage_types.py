# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.storage_types import StorageTypes

class TestStorageTypes(unittest.TestCase):
    """StorageTypes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StorageTypes:
        """Test StorageTypes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StorageTypes`
        """
        model = StorageTypes()
        if include_optional:
            return StorageTypes(
                items = [
                    dscc.models.device_types.deviceTypes(
                        description = 'HPE deviceType1 Storage', 
                        device_type = 'deviceType1', )
                    ],
                page_limit = 1,
                page_offset = 1,
                total = 56
            )
        else:
            return StorageTypes(
        )
        """

    def testStorageTypes(self):
        """Test StorageTypes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
