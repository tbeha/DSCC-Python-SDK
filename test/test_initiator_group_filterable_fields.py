# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.initiator_group_filterable_fields import InitiatorGroupFilterableFields

class TestInitiatorGroupFilterableFields(unittest.TestCase):
    """InitiatorGroupFilterableFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InitiatorGroupFilterableFields:
        """Test InitiatorGroupFilterableFields
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InitiatorGroupFilterableFields`
        """
        model = InitiatorGroupFilterableFields()
        if include_optional:
            return InitiatorGroupFilterableFields(
                access_protocol = 'iscsi',
                app_uuid = 'rfc4122.943f7dc1-5853-497c-b530-f689ccf1bf18',
                host_type = 'myobject-5',
                id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                name = 'myobject-5'
            )
        else:
            return InitiatorGroupFilterableFields(
        )
        """

    def testInitiatorGroupFilterableFields(self):
        """Test InitiatorGroupFilterableFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
