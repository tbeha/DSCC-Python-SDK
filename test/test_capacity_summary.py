# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.capacity_summary import CapacitySummary

class TestCapacitySummary(unittest.TestCase):
    """CapacitySummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CapacitySummary:
        """Test CapacitySummary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CapacitySummary`
        """
        model = CapacitySummary()
        if include_optional:
            return CapacitySummary(
                free = 56,
                total = 56
            )
        else:
            return CapacitySummary(
        )
        """

    def testCapacitySummary(self):
        """Test CapacitySummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
