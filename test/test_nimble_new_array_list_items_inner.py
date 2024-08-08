# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.nimble_new_array_list_items_inner import NimbleNewArrayListItemsInner

class TestNimbleNewArrayListItemsInner(unittest.TestCase):
    """NimbleNewArrayListItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NimbleNewArrayListItemsInner:
        """Test NimbleNewArrayListItemsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NimbleNewArrayListItemsInner`
        """
        model = NimbleNewArrayListItemsInner()
        if include_optional:
            return NimbleNewArrayListItemsInner(
                id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                model = 'myobject-5',
                name = 'NimbleArray',
                pool_id = '2a0df0fe6f7dc7bb16000000000000000000004817',
                serial = 'AC-109084',
                all_flash = False,
                allow_lower_limits = True,
                available_bytes = 1234,
                brand = 'myobject-5',
                common_resource_attributes = dscc.models.nimble_common_resource_attributes.NimbleCommonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                create_pool = True,
                creation_time = 3400,
                ctrlr_a_support_ip = '128.0.0.1',
                ctrlr_b_support_ip = '128.0.0.1',
                customer_id = 'string',
                dedupe_capacity_bytes = 1234,
                dedupe_usage_bytes = 1234,
                extended_model = 'myobject-5',
                fc_port_count = 1234,
                force = False,
                full_name = 'myobject-5',
                generation = 0,
                gig_nic_port_count = 1234,
                group_state = 'initialized',
                is_fully_dedupe_capable = False,
                is_sfa = False,
                is_supported_hw_config = True,
                last_modified = 3400,
                model_sub_type = 'VMWare',
                nic_list = [
                    dscc.models.nic_details.NICDetails(
                        data_ip = '128.0.0.1', 
                        name = 'NICName', 
                        subnet_label = '255.255.255.0', 
                        tagged = True, )
                    ],
                oem = 'myobject-5',
                pending_delete_bytes = 1234,
                pool_description = '99.9999% availability',
                pool_name = 'myobject-5',
                public_key = dscc.models.public_key_details.PublicKeyDetails(
                    key = 'DAQABAAABAQDR7pnlz5kehtrqNT9jIDP3KEVZdrYG64DH0ogJwLBM5fF27n/kssZt/NgcstPa2VvE6QTJQqW+3', 
                    key_name = 'root@abc', 
                    key_type = 'rsa', ),
                raw_capacity_bytes = 1234,
                resource_uri = '/api/v1/storage-systems/device-type2/2a0df0fe6f7dc7bb16000000000000000000004817',
                role = 'leader',
                search_name = 'vol:1',
                secondary_mgmt_ip = '128.0.0.1',
                snap_compression = 9.18,
                snap_saved_bytes = 1234,
                snap_space_reduction = 9.18,
                snap_usage_bytes = 1234,
                snap_usage_uncompressed_bytes = 1234,
                status = 'reachable',
                ten_gig_sfp_nic_port_count = 1234,
                ten_gig_t_nic_port_count = 1234,
                upgrade = dscc.models.upgrade_details.UpgradeDetails(
                    messages = [
                        dscc.models.nimble_error_with_arguments.NimbleErrorWithArguments(
                            code = 13, 
                            severity = 'info', 
                            text = 'Error occurred.', )
                        ], 
                    stage = 'finish', 
                    state = 'in_progress', 
                    type = 'offline', ),
                usable_cache_capacity_bytes = 1234,
                usable_capacity_bytes = 1234,
                usage = 1234,
                usage_valid = True,
                version = 'myobject-5',
                vol_compression = 9.18,
                vol_saved_bytes = 1234,
                vol_usage_bytes = 1234,
                vol_usage_uncompressed_bytes = 1234,
                zconf_ipaddrs = [
                    dscc.models.z_conf_i_paddrs.ZConfIPaddrs(
                        ip_addr = '128.0.0.1', )
                    ]
            )
        else:
            return NimbleNewArrayListItemsInner(
        )
        """

    def testNimbleNewArrayListItemsInner(self):
        """Test NimbleNewArrayListItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
