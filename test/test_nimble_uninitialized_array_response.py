# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_uninitialized_array_response import NimbleUninitializedArrayResponse

class TestNimbleUninitializedArrayResponse(unittest.TestCase):
    """NimbleUninitializedArrayResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleUninitializedArrayResponse:
        """Test NimbleUninitializedArrayResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleUninitializedArrayResponse`
        """
        model = NimbleUninitializedArrayResponse()
        if include_optional:
            return NimbleUninitializedArrayResponse(
                items = [
                    dscc.models.uninitialized_array_response.UninitializedArrayResponse(
                        all_flash = True, 
                        array_name = 'Nimble Array056', 
                        associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817","type":"storage-systems"}], 
                        console_uri = 'data-ops-manager/storage-systems/device-type2/0041aca441479e44e5000000000000000000000001/uninitialized-arrays/c463732d3633346563330000000000000000000000', 
                        count_of_fc_ports = 1234, 
                        customer_id = 'string', 
                        dedupe_configurable = True, 
                        generation = 0, 
                        id = 'c463732d3633346563330000000000000000000000', 
                        model_str = 'myobject-5', 
                        resource_uri = '/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817', 
                        serial = 'AC-109084', 
                        type = 'string', 
                        version = 'myobject-5', 
                        zconf_ipaddrs = [
                            dscc.models.nimble_z_conf_ip.NimbleZConfIP(
                                ip_addr = '127.0.0.1', )
                            ], )
                    ],
                page_limit = 1,
                page_offset = 1,
                total = 1
            )
        else:
            return NimbleUninitializedArrayResponse(
        )
        """

    def testNimbleUninitializedArrayResponse(self):
        """Test NimbleUninitializedArrayResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
