# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_replication_partner_common_fields_policies import DeviceType4ReplicationPartnerCommonFieldsPolicies

class TestDeviceType4ReplicationPartnerCommonFieldsPolicies(unittest.TestCase):
    """DeviceType4ReplicationPartnerCommonFieldsPolicies unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4ReplicationPartnerCommonFieldsPolicies:
        """Test DeviceType4ReplicationPartnerCommonFieldsPolicies
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4ReplicationPartnerCommonFieldsPolicies`
        """
        model = DeviceType4ReplicationPartnerCommonFieldsPolicies()
        if include_optional:
            return DeviceType4ReplicationPartnerCommonFieldsPolicies(
                mirror_config = True
            )
        else:
            return DeviceType4ReplicationPartnerCommonFieldsPolicies(
        )
        """

    def testDeviceType4ReplicationPartnerCommonFieldsPolicies(self):
        """Test DeviceType4ReplicationPartnerCommonFieldsPolicies"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
