# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4allocation_ha import DeviceType4allocationHA

class TestDeviceType4allocationHA(unittest.TestCase):
    """DeviceType4allocationHA unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4allocationHA:
        """Test DeviceType4allocationHA
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4allocationHA`
        """
        model = DeviceType4allocationHA()
        if include_optional:
            return DeviceType4allocationHA(
                default = '',
                key = ''
            )
        else:
            return DeviceType4allocationHA(
        )
        """

    def testDeviceType4allocationHA(self):
        """Test DeviceType4allocationHA"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
