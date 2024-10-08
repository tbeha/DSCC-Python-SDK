# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_disk_loop_inner import DeviceType4DiskLoopInner

class TestDeviceType4DiskLoopInner(unittest.TestCase):
    """DeviceType4DiskLoopInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4DiskLoopInner:
        """Test DeviceType4DiskLoopInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4DiskLoopInner`
        """
        model = DeviceType4DiskLoopInner()
        if include_optional:
            return DeviceType4DiskLoopInner(
                degraded = False,
                disabled = False,
                port = dscc.models.device_type4_disk_port_position.DeviceType4DiskPortPosition(
                    node = 0, 
                    slot = 0, ),
                primary = False
            )
        else:
            return DeviceType4DiskLoopInner(
        )
        """

    def testDeviceType4DiskLoopInner(self):
        """Test DeviceType4DiskLoopInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
