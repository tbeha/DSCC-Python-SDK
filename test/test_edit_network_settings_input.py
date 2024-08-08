# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.edit_network_settings_input import EditNetworkSettingsInput

class TestEditNetworkSettingsInput(unittest.TestCase):
    """EditNetworkSettingsInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditNetworkSettingsInput:
        """Test EditNetworkSettingsInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditNetworkSettingsInput`
        """
        model = EditNetworkSettingsInput()
        if include_optional:
            return EditNetworkSettingsInput(
                dns_addresses = [
                    ''
                    ],
                ipv4_address = '',
                ipv4_gateway = '',
                ipv4_subnet_mask = '',
                ipv6_address = '',
                ipv6_gateway = '',
                ipv6_prefix_len = '',
                proxy_params = dscc.models.edit_network_settings_input_proxy_params.editNetworkSettingsInput_proxyParams(
                    authentication_required = '', 
                    proxy_password = '', 
                    proxy_port = 56, 
                    proxy_protocol = '', 
                    proxy_server = '', 
                    proxy_user = '', )
            )
        else:
            return EditNetworkSettingsInput(
        )
        """

    def testEditNetworkSettingsInput(self):
        """Test EditNetworkSettingsInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
