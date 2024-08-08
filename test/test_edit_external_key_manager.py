# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.edit_external_key_manager import EditExternalKeyManager

class TestEditExternalKeyManager(unittest.TestCase):
    """EditExternalKeyManager unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditExternalKeyManager:
        """Test EditExternalKeyManager
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditExternalKeyManager`
        """
        model = EditExternalKeyManager()
        if include_optional:
            return EditExternalKeyManager(
                description = '1234',
                hostname = 'ext.key.manager.com',
                id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                name = 'myobject-5',
                password = 'abc123',
                port = 1234,
                protocol = 'KMIP1_0',
                username = 'user1'
            )
        else:
            return EditExternalKeyManager(
        )
        """

    def testEditExternalKeyManager(self):
        """Test EditExternalKeyManager"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
