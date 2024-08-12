# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_host_state_detailed import DeviceType4HostStateDetailed

class TestDeviceType4HostStateDetailed(unittest.TestCase):
    """DeviceType4HostStateDetailed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4HostStateDetailed:
        """Test DeviceType4HostStateDetailed
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4HostStateDetailed`
        """
        model = DeviceType4HostStateDetailed()
        if include_optional:
            return DeviceType4HostStateDetailed(
                args = [
                    ''
                    ],
                default = 'Host sltestish',
                key = 'HOST_NAME',
                localized_text = 'Localized text of the resource capabilities'
            )
        else:
            return DeviceType4HostStateDetailed(
        )
        """

    def testDeviceType4HostStateDetailed(self):
        """Test DeviceType4HostStateDetailed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
