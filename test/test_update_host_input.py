# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.update_host_input import UpdateHostInput

class TestUpdateHostInput(unittest.TestCase):
    """UpdateHostInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateHostInput:
        """Test UpdateHostInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateHostInput`
        """
        model = UpdateHostInput()
        if include_optional:
            return UpdateHostInput(
                initiators_to_create = [
                    dscc.models.initiator_input.InitiatorInput(
                        address = 'iqn.1998-01.com.vmware:61f7c688-3e93-d360-8043-70106f7a7e18-0cba0054', 
                        driver_version = '4.1', 
                        firmware_version = '10.0', 
                        hba_model = 'model-5', 
                        host_speed = 1000, 
                        ip_address = '15.212.100.100', 
                        name = 'init1', 
                        protocol = 'iSCSI', 
                        vendor = 'hpe', )
                    ],
                name = 'host1',
                updated_initiators = [
                    ''
                    ]
            )
        else:
            return UpdateHostInput(
        )
        """

    def testUpdateHostInput(self):
        """Test UpdateHostInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
