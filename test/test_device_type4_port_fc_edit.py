# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_port_fc_edit import DeviceType4PortFCEdit

class TestDeviceType4PortFCEdit(unittest.TestCase):
    """DeviceType4PortFCEdit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4PortFCEdit:
        """Test DeviceType4PortFCEdit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4PortFCEdit`
        """
        model = DeviceType4PortFCEdit()
        if include_optional:
            return DeviceType4PortFCEdit(
                config_mode = 'Host',
                connection_type = 'Loop',
                interupt_coalesce = True,
                label = 'FCPort1',
                speed_configured = '8',
                unique_wwn = True,
                vcn = True
            )
        else:
            return DeviceType4PortFCEdit(
        )
        """

    def testDeviceType4PortFCEdit(self):
        """Test DeviceType4PortFCEdit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
