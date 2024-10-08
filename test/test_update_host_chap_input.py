# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.update_host_chap_input import UpdateHostChapInput

class TestUpdateHostChapInput(unittest.TestCase):
    """UpdateHostChapInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateHostChapInput:
        """Test UpdateHostChapInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateHostChapInput`
        """
        model = UpdateHostChapInput()
        if include_optional:
            return UpdateHostChapInput(
                items = [
                    dscc.models.host_chap_input_object.HostChapInputObject(
                        initiator_chap_enabled = True, 
                        initiator_chap_name = 'chapnameSetDSCC', 
                        initiator_encrypted_chap_secret = 'dGVzdGNoYXBzZWNyZXQ', 
                        system = 'SGH014XGSP', 
                        target_chap_enabled = True, 
                        target_chap_name = 'chapnameSetDSCC', 
                        target_encrypted_chap_secret = 'dGVzdGNoYXBzZWNyZXQ', )
                    ]
            )
        else:
            return UpdateHostChapInput(
        )
        """

    def testUpdateHostChapInput(self):
        """Test UpdateHostChapInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
