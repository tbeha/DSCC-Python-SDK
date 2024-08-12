# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_health_status_list_items_inner import NimbleHealthStatusListItemsInner

class TestNimbleHealthStatusListItemsInner(unittest.TestCase):
    """NimbleHealthStatusListItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleHealthStatusListItemsInner:
        """Test NimbleHealthStatusListItemsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleHealthStatusListItemsInner`
        """
        model = NimbleHealthStatusListItemsInner()
        if include_optional:
            return NimbleHealthStatusListItemsInner(
                array_id = 'active',
                context = 'active',
                ctrlr_id = 'active',
                id = '1300000000000004d30000000000000001',
                scope = 'array',
                associated_links = [{resourceUri=/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817, type=storage-systems}],
                common_resource_attributes = dscc.models.nimble_common_resource_attributes.NimbleCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                customer_id = 'string',
                element_result = dscc.models.nimble_hcf_result.NimbleHCFResult(
                    element_name = 'nimblevega', 
                    error_list = [
                        'error1'
                        ], 
                    messages = [
                        dscc.models.nimble_error_with_arguments.NimbleErrorWithArguments(
                            code = 13, 
                            severity = 'info', 
                            text = 'Error occurred.', )
                        ], ),
                generation = 0,
                on_demand = False,
                resource_uri = '/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817'
            )
        else:
            return NimbleHealthStatusListItemsInner(
        )
        """

    def testNimbleHealthStatusListItemsInner(self):
        """Test NimbleHealthStatusListItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
