# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4manufacturing import DeviceType4manufacturing

class TestDeviceType4manufacturing(unittest.TestCase):
    """DeviceType4manufacturing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4manufacturing:
        """Test DeviceType4manufacturing
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4manufacturing`
        """
        model = DeviceType4manufacturing()
        if include_optional:
            return DeviceType4manufacturing(
                assembly_rev = '002*',
                check_sum = '--',
                hpe_model_name = 'HPE 3PAR 600 2S Node',
                manufacturer = 'XYRATEX',
                model = '0974244-06',
                saleable_part_number = '0974244-06',
                saleable_serial_number = '4UW0002941',
                serial_number = 'PMW0974244G4T88',
                spare_part_number = 'P04031-001'
            )
        else:
            return DeviceType4manufacturing(
        )
        """

    def testDeviceType4manufacturing(self):
        """Test DeviceType4manufacturing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
