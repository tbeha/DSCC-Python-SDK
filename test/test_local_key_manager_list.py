# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.local_key_manager_list import LocalKeyManagerList

class TestLocalKeyManagerList(unittest.TestCase):
    """LocalKeyManagerList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LocalKeyManagerList:
        """Test LocalKeyManagerList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LocalKeyManagerList`
        """
        model = LocalKeyManagerList()
        if include_optional:
            return LocalKeyManagerList(
                items = [
                    dscc.models.local_key_manager.LocalKeyManager()
                    ],
                page_limit = 1,
                page_offset = 1,
                request_uri = 'api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817/local-key-manager',
                total = 1
            )
        else:
            return LocalKeyManagerList(
        )
        """

    def testLocalKeyManagerList(self):
        """Test LocalKeyManagerList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
