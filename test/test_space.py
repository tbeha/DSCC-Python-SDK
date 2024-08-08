# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.space import Space

class TestSpace(unittest.TestCase):
    """Space unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Space:
        """Test Space
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Space`
        """
        model = Space()
        if include_optional:
            return Space(
                free_mi_b = 1.337,
                grown_mi_b = 1.337,
                raw_reserved_mi_b = 1.337,
                reclaimed_mi_b = 1.337,
                reserved_mi_b = 1.337,
                total_mi_b = 1.337,
                used_mi_b = 1.337
            )
        else:
            return Space(
        )
        """

    def testSpace(self):
        """Test Space"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
