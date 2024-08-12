# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.local_key_manager import LocalKeyManager

class TestLocalKeyManager(unittest.TestCase):
    """LocalKeyManager unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LocalKeyManager:
        """Test LocalKeyManager
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LocalKeyManager`
        """
        model = LocalKeyManager()
        if include_optional:
            return LocalKeyManager(
                id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                name = 'default',
                active = True,
                common_resource_attributes = dscc.models.nimble_common_resource_attributes.NimbleCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'null',
                customer_id = 'fc5f41652a53497e88cdcebc715cc1cf',
                generation = 0,
                purge_age = 1234,
                resource_uri = '/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817',
                type = 'string'
            )
        else:
            return LocalKeyManager(
        )
        """

    def testLocalKeyManager(self):
        """Test LocalKeyManager"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
