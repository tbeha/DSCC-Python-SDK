# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.recommendation_list import RecommendationList

class TestRecommendationList(unittest.TestCase):
    """RecommendationList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecommendationList:
        """Test RecommendationList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecommendationList`
        """
        model = RecommendationList()
        if include_optional:
            return RecommendationList(
                capacity_info = dscc.models.capacity_info_solo.capacityInfoSolo(
                    capacity_summary = dscc.models.capacity_summary.capacitySummary(
                        free = 56, 
                        total = 56, ), ),
                id = 'RTYTY123',
                mgmt_ip = '1.2.3.4',
                name = 'system_Name',
                product_family = 'deviceType1',
                state = 'NORMAL',
                system_wwn = '2FF70002AC018D94'
            )
        else:
            return RecommendationList(
        )
        """

    def testRecommendationList(self):
        """Test RecommendationList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
