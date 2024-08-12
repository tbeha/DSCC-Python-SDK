# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.insights_response import InsightsResponse

class TestInsightsResponse(unittest.TestCase):
    """InsightsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsResponse:
        """Test InsightsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsResponse`
        """
        model = InsightsResponse()
        if include_optional:
            return InsightsResponse(
                members = [
                    dscc.models.insights_data.InsightsData(
                        category = 'CAPACITY', 
                        cause = '', 
                        create_time = 56, 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        details = dscc.models.insight_details.InsightDetails(
                            additional_details = '', 
                            end_time = 56, 
                            start_time = 56, ), 
                        id = '', 
                        insight_details_uri = '', 
                        insight_uri = '', 
                        last_updated_time = 56, 
                        remediation = '', 
                        resource_details = dscc.models.resource_detail.ResourceDetail(
                            resource_type = '', 
                            resource_uid = '', 
                            resource_uri = '', ), 
                        score = 56, 
                        severity = 'CRITICAL', 
                        state = '', 
                        sub_type = '', 
                        symptom = '', 
                        system_details = dscc.models.system_details.SystemDetails(
                            system_id = '', 
                            system_uri = '', 
                            type = '', ), 
                        system_id = '', 
                        tenant_id = '', 
                        title = '', 
                        type = 'TIME_UNTIL_FULL', 
                        value = 1.337, )
                    ]
            )
        else:
            return InsightsResponse(
        )
        """

    def testInsightsResponse(self):
        """Test InsightsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
