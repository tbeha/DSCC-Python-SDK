# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.allocation import Allocation

class TestAllocation(unittest.TestCase):
    """Allocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Allocation:
        """Test Allocation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Allocation`
        """
        model = Allocation()
        if include_optional:
            return Allocation(
                ha = dscc.models.device_type4allocation_ha.DeviceType4allocation_HA(
                    default = '', 
                    key = '', ),
                raid_type = 'RAID_SIX',
                chunklet_pos_pref = 'Position1',
                device_speed = dscc.models.device_type4allocation_device_speed.DeviceType4allocation_deviceSpeed(
                    default = '', 
                    key = '', 
                    text = '', 
                    value = 56, ),
                device_type = 'DEVICE_TYPE_SSD',
                disk_filter = 'test',
                requested_ha = dscc.models.device_type4allocation_ha.DeviceType4allocation_HA(
                    default = '', 
                    key = '', ),
                set_size = '6 data, 2 parity',
                step_size = -1
            )
        else:
            return Allocation(
        )
        """

    def testAllocation(self):
        """Test Allocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
