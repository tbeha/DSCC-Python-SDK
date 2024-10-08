# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_replication_partner import DeviceType4ReplicationPartner

class TestDeviceType4ReplicationPartner(unittest.TestCase):
    """DeviceType4ReplicationPartner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4ReplicationPartner:
        """Test DeviceType4ReplicationPartner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4ReplicationPartner`
        """
        model = DeviceType4ReplicationPartner()
        if include_optional:
            return DeviceType4ReplicationPartner(
                async_partner = 'CS2-A630-SVQ8',
                id = '5a5ce66d4814a5e5156de428abb0a589',
                is_active_sync_supported = True,
                is_peer_persistance_supported = True,
                min_async_rpo = 30,
                name = 's2930',
                resource_uri = '/api/v1/storage-systems/device-type4/7CE815P2BH/replicationpartners/5a5ce66d4814a5e5156de428abb0a589',
                sync_partner = 'CS2-A630-SVQ8_1'
            )
        else:
            return DeviceType4ReplicationPartner(
        )
        """

    def testDeviceType4ReplicationPartner(self):
        """Test DeviceType4ReplicationPartner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
