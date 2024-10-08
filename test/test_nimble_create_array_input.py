# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_create_array_input import NimbleCreateArrayInput

class TestNimbleCreateArrayInput(unittest.TestCase):
    """NimbleCreateArrayInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleCreateArrayInput:
        """Test NimbleCreateArrayInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleCreateArrayInput`
        """
        model = NimbleCreateArrayInput()
        if include_optional:
            return NimbleCreateArrayInput(
                allow_lower_limits = False,
                create_pool = False,
                ctrlr_a_support_ip = '128.0.0.1',
                ctrlr_b_support_ip = '128.0.0.1',
                dedupe_disabled = False,
                name = 'NimbleArray',
                nic_list = [
                    dscc.models.nic_details.NICDetails(
                        data_ip = '128.0.0.1', 
                        name = 'NICName', 
                        subnet_label = '255.255.255.0', 
                        tagged = True, )
                    ],
                pool_description = '99.9999% availability',
                pool_name = 'myobject-5',
                secondary_mgmt_ip = '128.0.0.1',
                serial = 'AC-109084'
            )
        else:
            return NimbleCreateArrayInput(
                ctrlr_a_support_ip = '128.0.0.1',
                ctrlr_b_support_ip = '128.0.0.1',
                name = 'NimbleArray',
                nic_list = [
                    dscc.models.nic_details.NICDetails(
                        data_ip = '128.0.0.1', 
                        name = 'NICName', 
                        subnet_label = '255.255.255.0', 
                        tagged = True, )
                    ],
                pool_name = 'myobject-5',
                serial = 'AC-109084',
        )
        """

    def testNimbleCreateArrayInput(self):
        """Test NimbleCreateArrayInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
