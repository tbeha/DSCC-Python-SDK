# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_locate_input import DeviceType4LocateInput

class TestDeviceType4LocateInput(unittest.TestCase):
    """DeviceType4LocateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4LocateInput:
        """Test DeviceType4LocateInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4LocateInput`
        """
        model = DeviceType4LocateInput()
        if include_optional:
            return DeviceType4LocateInput(
                locate = True
            )
        else:
            return DeviceType4LocateInput(
        )
        """

    def testDeviceType4LocateInput(self):
        """Test DeviceType4LocateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
