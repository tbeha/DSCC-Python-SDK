# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.private import Private

class TestPrivate(unittest.TestCase):
    """Private unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Private:
        """Test Private
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Private`
        """
        model = Private()
        if include_optional:
            return Private(
                reserved = 1.337,
                reserved_v_vols = 1.337,
                total = 1.337
            )
        else:
            return Private(
        )
        """

    def testPrivate(self):
        """Test Private"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
