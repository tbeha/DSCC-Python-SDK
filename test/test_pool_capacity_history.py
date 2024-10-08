# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.pool_capacity_history import PoolCapacityHistory

class TestPoolCapacityHistory(unittest.TestCase):
    """PoolCapacityHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PoolCapacityHistory:
        """Test PoolCapacityHistory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PoolCapacityHistory`
        """
        model = PoolCapacityHistory()
        if include_optional:
            return PoolCapacityHistory(
                common_resource_attributes = dscc.models.nimble_common_resource_attributes.NimbleCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                count = 127,
                request_uri = '/api/v1/storage-systems/device-type2/00473102de2f5f39d8000000000000000000000001/storage-pools/37473102de2f5f39d8000000000000000000000027/capacity-history',
                series_data = [
                    dscc.models.nimblecapacity_series_data.nimblecapacitySeriesData(
                        savings = 5, 
                        timestamp = 1605063600, 
                        usage = 4, )
                    ]
            )
        else:
            return PoolCapacityHistory(
        )
        """

    def testPoolCapacityHistory(self):
        """Test PoolCapacityHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
