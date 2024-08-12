# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.protection_policy_secondary_remote_input_schema import ProtectionPolicySecondaryRemoteInputSchema

class TestProtectionPolicySecondaryRemoteInputSchema(unittest.TestCase):
    """ProtectionPolicySecondaryRemoteInputSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProtectionPolicySecondaryRemoteInputSchema:
        """Test ProtectionPolicySecondaryRemoteInputSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProtectionPolicySecondaryRemoteInputSchema`
        """
        model = ProtectionPolicySecondaryRemoteInputSchema()
        if include_optional:
            return ProtectionPolicySecondaryRemoteInputSchema(
                partner_id = 'afb4961e47212e5bc88dd35db5be5c83',
                partner_name = 'IP_target',
                replication_type = 'periodic'
            )
        else:
            return ProtectionPolicySecondaryRemoteInputSchema(
                partner_id = 'afb4961e47212e5bc88dd35db5be5c83',
                partner_name = 'IP_target',
                replication_type = 'periodic',
        )
        """

    def testProtectionPolicySecondaryRemoteInputSchema(self):
        """Test ProtectionPolicySecondaryRemoteInputSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
