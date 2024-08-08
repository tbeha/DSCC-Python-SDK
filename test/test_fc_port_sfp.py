# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.fc_port_sfp import FcPortSfp

class TestFcPortSfp(unittest.TestCase):
    """FcPortSfp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FcPortSfp:
        """Test FcPortSfp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FcPortSfp`
        """
        model = FcPortSfp()
        if include_optional:
            return FcPortSfp(
                fw_version = '',
                manufacturing = dscc.models.manufacturing_single.manufacturingSingle(
                    assembly_rev = '002*', 
                    check_sum = '--', 
                    hpe_model_name = 'HPE 3PAR 600 2S Node', 
                    manufacturer = 'XYRATEX', 
                    model = '0974244-06', 
                    saleable_part_number = '0974244-06', 
                    saleable_serial_number = '4UW0002941', 
                    serial_number = 'PMW0974244G4T88', 
                    spare_part_number = 'P04031-001', ),
                name = '',
                qualified = True,
                rx_loss_pin = '',
                rx_power_low = True,
                speed = 1,
                state = dscc.models.state.STATE(
                    detailed = [
                        ''
                        ], 
                    overall = 'STATE_NORMAL', ),
                tx_disable_pin = '',
                tx_fault_pin = ''
            )
        else:
            return FcPortSfp(
        )
        """

    def testFcPortSfp(self):
        """Test FcPortSfp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
