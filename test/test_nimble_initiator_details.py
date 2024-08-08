# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_initiator_details import NimbleInitiatorDetails

class TestNimbleInitiatorDetails(unittest.TestCase):
    """NimbleInitiatorDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleInitiatorDetails:
        """Test NimbleInitiatorDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleInitiatorDetails`
        """
        model = NimbleInitiatorDetails()
        if include_optional:
            return NimbleInitiatorDetails(
                access_protocol = '',
                alias = 'my_initiator-4',
                associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817","type":"storage-systems"}],
                chapuser_id = '011c9973433673c3db000000000000000000000000',
                common_resource_attributes = dscc.models.nimble_common_resource_attributes.NimbleCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                console_uri = 'null',
                creation_time = 3400,
                customer_id = 'string',
                generation = 0,
                id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                initiator_group_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                initiator_group_name = 'myobject-5',
                ip_address = 'iqn.2007-11.com.storage:zmytestvol1-v0df0fe6f7dc7bb16.0000016b.70374579',
                iqn = '',
                label = 'myobject-5',
                last_modified = 3400,
                override_existing_alias = True,
                request_uri = 'api/v1/storage-systems/devicetype2/2a0df0fe6f7dc7bb16000000000000000000004817/host-initiators/2a0df0fe6f7dc7bb16000000000000000000004007',
                resource_uri = '/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817',
                sc_host_initiator_id = '1223f5s',
                type = 'string',
                wwpn = 'af:32:f1:20:bc:ba:43:1a'
            )
        else:
            return NimbleInitiatorDetails(
        )
        """

    def testNimbleInitiatorDetails(self):
        """Test NimbleInitiatorDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
