# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_disk_capacity import DeviceType4DiskCapacity

class TestDeviceType4DiskCapacity(unittest.TestCase):
    """DeviceType4DiskCapacity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4DiskCapacity:
        """Test DeviceType4DiskCapacity
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4DiskCapacity`
        """
        model = DeviceType4DiskCapacity()
        if include_optional:
            return DeviceType4DiskCapacity(
                allocated_mi_b = 595968,
                failed_mi_b = 0,
                free_mi_b = 1233920,
                total_mi_b = 595968,
                unavailable_mi_b = 0
            )
        else:
            return DeviceType4DiskCapacity(
        )
        """

    def testDeviceType4DiskCapacity(self):
        """Test DeviceType4DiskCapacity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
