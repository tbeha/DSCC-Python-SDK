# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_controller_list import NimbleControllerList

class TestNimbleControllerList(unittest.TestCase):
    """NimbleControllerList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleControllerList:
        """Test NimbleControllerList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleControllerList`
        """
        model = NimbleControllerList()
        if include_optional:
            return NimbleControllerList(
                items = [
                    null
                    ],
                page_limit = 1,
                page_offset = 1,
                request_uri = 'api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817/controllers',
                total = 1
            )
        else:
            return NimbleControllerList(
        )
        """

    def testNimbleControllerList(self):
        """Test NimbleControllerList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
