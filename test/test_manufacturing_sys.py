# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.manufacturing_sys import ManufacturingSys

class TestManufacturingSys(unittest.TestCase):
    """ManufacturingSys unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManufacturingSys:
        """Test ManufacturingSys
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManufacturingSys`
        """
        model = ManufacturingSys()
        if include_optional:
            return ManufacturingSys(
                assembly_rev = '',
                check_sum = '',
                hpe_model_name = '',
                manufacturer = 'HPE 3PAR',
                model = 'HPE_3PAR 8400',
                saleable_part_number = '',
                saleable_serial_number = '',
                serial_number = 'MXN5442108',
                spare_part_number = ''
            )
        else:
            return ManufacturingSys(
        )
        """

    def testManufacturingSys(self):
        """Test ManufacturingSys"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
