# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_edit_array_net import NimbleEditArrayNet

class TestNimbleEditArrayNet(unittest.TestCase):
    """NimbleEditArrayNet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleEditArrayNet:
        """Test NimbleEditArrayNet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleEditArrayNet`
        """
        model = NimbleEditArrayNet()
        if include_optional:
            return NimbleEditArrayNet(
                ctrlr_a_support_ip = '127.0.0.102',
                ctrlr_b_support_ip = '127.0.0.103',
                name = 'g1a16',
                nic_list = [
                    dscc.models.nimble_nic.NimbleNIC(
                        data_ip = '127.0.0.102', 
                        name = 'eth1', 
                        subnet_label = 'subnet1', 
                        tagged = True, )
                    ]
            )
        else:
            return NimbleEditArrayNet(
        )
        """

    def testNimbleEditArrayNet(self):
        """Test NimbleEditArrayNet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
