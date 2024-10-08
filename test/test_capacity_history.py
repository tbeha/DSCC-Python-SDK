# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.capacity_history import CapacityHistory

class TestCapacityHistory(unittest.TestCase):
    """CapacityHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CapacityHistory:
        """Test CapacityHistory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CapacityHistory`
        """
        model = CapacityHistory()
        if include_optional:
            return CapacityHistory(
                capacity_data = dscc.models.capacity_history_capacity_data.capacityHistory_capacityData(
                    customer_id = 'string', 
                    items = [
                        dscc.models.capacity_series_data.capacitySeriesData(
                            timestamp_ms = 1605063600, 
                            usage_mi_b = 4, )
                        ], 
                    total = 1, ),
                common_resource_attributes = dscc.models.primera_common_resource_attributes.primeraCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                end_time = 1625209133,
                request_uri = '/v1/storage-systems/device-type1/SGH014XGSP/capacity-history',
                start_time = 1625122733
            )
        else:
            return CapacityHistory(
        )
        """

    def testCapacityHistory(self):
        """Test CapacityHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
