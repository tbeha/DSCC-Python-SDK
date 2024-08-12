# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.headroom_utilization import HeadroomUtilization

class TestHeadroomUtilization(unittest.TestCase):
    """HeadroomUtilization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HeadroomUtilization:
        """Test HeadroomUtilization
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HeadroomUtilization`
        """
        model = HeadroomUtilization()
        if include_optional:
            return HeadroomUtilization(
                average_headroom_utilization_data = dscc.models.headroom_utilization_average_headroom_utilization_data.headroomUtilization_averageHeadroomUtilizationData(
                    headroom = 20.3, 
                    headroom_utilization = 'low', ),
                customer_id = '',
                end_time = 1669880791,
                granularity_in_min = 60,
                headroom_utilization_data = [
                    dscc.models.headroom_data.headroomData(
                        level = 'low', 
                        timestamp_ms = 1669794420000, 
                        value = 0.47, )
                    ],
                request_uri = '/api/v1/storage-systems/device-type1/ABC239XFZ9/headroom-utilization',
                start_time = 1669794391
            )
        else:
            return HeadroomUtilization(
        )
        """

    def testHeadroomUtilization(self):
        """Test HeadroomUtilization"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
