# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.encryption_restore_action_input import EncryptionRestoreActionInput

class TestEncryptionRestoreActionInput(unittest.TestCase):
    """EncryptionRestoreActionInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EncryptionRestoreActionInput:
        """Test EncryptionRestoreActionInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EncryptionRestoreActionInput`
        """
        model = EncryptionRestoreActionInput()
        if include_optional:
            return EncryptionRestoreActionInput(
                key = 'key',
                parameters = dscc.models.encryption_params.EncryptionParams(
                    enable_ekm = True, 
                    password = 'testpassword', )
            )
        else:
            return EncryptionRestoreActionInput(
        )
        """

    def testEncryptionRestoreActionInput(self):
        """Test EncryptionRestoreActionInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
