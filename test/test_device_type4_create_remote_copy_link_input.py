# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_create_remote_copy_link_input import DeviceType4CreateRemoteCopyLinkInput

class TestDeviceType4CreateRemoteCopyLinkInput(unittest.TestCase):
    """DeviceType4CreateRemoteCopyLinkInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4CreateRemoteCopyLinkInput:
        """Test DeviceType4CreateRemoteCopyLinkInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4CreateRemoteCopyLinkInput`
        """
        model = DeviceType4CreateRemoteCopyLinkInput()
        if include_optional:
            return DeviceType4CreateRemoteCopyLinkInput(
                address = '10.100.65.128',
                port_pos = dscc.models.create_remote_copy_link_input_port_pos.CreateRemoteCopyLinkInput_portPos(
                    node = 0, 
                    port = 3, 
                    slot = 1, ),
                target_name = 'Sample_RCTarget',
                type = 1
            )
        else:
            return DeviceType4CreateRemoteCopyLinkInput(
                address = '10.100.65.128',
                port_pos = dscc.models.create_remote_copy_link_input_port_pos.CreateRemoteCopyLinkInput_portPos(
                    node = 0, 
                    port = 3, 
                    slot = 1, ),
                target_name = 'Sample_RCTarget',
                type = 1,
        )
        """

    def testDeviceType4CreateRemoteCopyLinkInput(self):
        """Test DeviceType4CreateRemoteCopyLinkInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
