# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4create_volume import DeviceType4createVolume

class TestDeviceType4createVolume(unittest.TestCase):
    """DeviceType4createVolume unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4createVolume:
        """Test DeviceType4createVolume
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4createVolume`
        """
        model = DeviceType4createVolume()
        if include_optional:
            return DeviceType4createVolume(
                destination_cpg = 'SSD_r6'
            )
        else:
            return DeviceType4createVolume(
        )
        """

    def testDeviceType4createVolume(self):
        """Test DeviceType4createVolume"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
