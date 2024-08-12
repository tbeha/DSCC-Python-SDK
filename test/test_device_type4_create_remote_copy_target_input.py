# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_create_remote_copy_target_input import DeviceType4CreateRemoteCopyTargetInput

class TestDeviceType4CreateRemoteCopyTargetInput(unittest.TestCase):
    """DeviceType4CreateRemoteCopyTargetInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4CreateRemoteCopyTargetInput:
        """Test DeviceType4CreateRemoteCopyTargetInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4CreateRemoteCopyTargetInput`
        """
        model = DeviceType4CreateRemoteCopyTargetInput()
        if include_optional:
            return DeviceType4CreateRemoteCopyTargetInput(
                disabled = True,
                name = 'sample_RCtarget',
                node_wwn = '2FF70002AC020DA1',
                port_pos_and_link = [
                    dscc.models.device_type4_port_pos_and_link_input.DeviceType4PortPosAndLinkInput(
                        link = '10.100.65.128', 
                        port_position = dscc.models.device_type4_port_position_input.DeviceType4PortPositionInput(
                            node = 0, 
                            port = 3, 
                            slot = 1, ), )
                    ],
                type = 1
            )
        else:
            return DeviceType4CreateRemoteCopyTargetInput(
                name = 'sample_RCtarget',
                port_pos_and_link = [
                    dscc.models.device_type4_port_pos_and_link_input.DeviceType4PortPosAndLinkInput(
                        link = '10.100.65.128', 
                        port_position = dscc.models.device_type4_port_position_input.DeviceType4PortPositionInput(
                            node = 0, 
                            port = 3, 
                            slot = 1, ), )
                    ],
                type = 1,
        )
        """

    def testDeviceType4CreateRemoteCopyTargetInput(self):
        """Test DeviceType4CreateRemoteCopyTargetInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
