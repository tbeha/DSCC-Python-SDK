# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.replication_partner_fields_with_filter import ReplicationPartnerFieldsWithFilter

class TestReplicationPartnerFieldsWithFilter(unittest.TestCase):
    """ReplicationPartnerFieldsWithFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReplicationPartnerFieldsWithFilter:
        """Test ReplicationPartnerFieldsWithFilter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReplicationPartnerFieldsWithFilter`
        """
        model = ReplicationPartnerFieldsWithFilter()
        if include_optional:
            return ReplicationPartnerFieldsWithFilter(
                id = '5a5ce66d4814a5e5156de428abb0a589',
                name = 'RCPartner12',
                replication_partner_type = 'FC',
                status = 'Ready'
            )
        else:
            return ReplicationPartnerFieldsWithFilter(
        )
        """

    def testReplicationPartnerFieldsWithFilter(self):
        """Test ReplicationPartnerFieldsWithFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
