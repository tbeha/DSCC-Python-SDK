# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_volume_capacity_history import DeviceType4VolumeCapacityHistory

class TestDeviceType4VolumeCapacityHistory(unittest.TestCase):
    """DeviceType4VolumeCapacityHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4VolumeCapacityHistory:
        """Test DeviceType4VolumeCapacityHistory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4VolumeCapacityHistory`
        """
        model = DeviceType4VolumeCapacityHistory()
        if include_optional:
            return DeviceType4VolumeCapacityHistory(
                capacity_data = dscc.models.device_type4_volume_capacity_history_capacity_data.DeviceType4VolumeCapacityHistory_capacityData(
                    customer_id = 'string', 
                    items = [
                        dscc.models.device_type4volume_capacity_series_data.DeviceType4volumeCapacitySeriesData(
                            actual_usage_mi_b = 25, 
                            host_written_capacity_mi_b = 20, 
                            timestamp_ms = 1605063600, )
                        ], 
                    total = 1, ),
                common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                end_time = 1625209133,
                request_uri = '/v1/storage-systems/device-type4/SGH014XGSP/volumes/a7c4e6593f51d0b98f0e40d7e6df04fd/capacity-history',
                start_time = 1625122733
            )
        else:
            return DeviceType4VolumeCapacityHistory(
        )
        """

    def testDeviceType4VolumeCapacityHistory(self):
        """Test DeviceType4VolumeCapacityHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
