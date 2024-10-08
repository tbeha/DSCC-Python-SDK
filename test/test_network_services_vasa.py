# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.network_services_vasa import NetworkServicesVasa

class TestNetworkServicesVasa(unittest.TestCase):
    """NetworkServicesVasa unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkServicesVasa:
        """Test NetworkServicesVasa
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkServicesVasa`
        """
        model = NetworkServicesVasa()
        if include_optional:
            return NetworkServicesVasa(
                items = dscc.models.vasa_details.vasaDetails(
                    associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type1/{uid}","type":"systems"}], 
                    system_id = '4UW0001540', 
                    vasa = dscc.models.vasa.vasa(
                        cert_mgmt = dscc.models.cert_mgmt.certMgmt(
                            default = 'server', 
                            key = 'VASA_CERTMGMT_MODE-1', ), 
                        cert_subject = 'Unknown', 
                        cert_thumbprint = 'Unknown', 
                        console_uri = 'data-ops-manager/storage-systems/device-type1/SGH014XGSP/settings/system-settings', 
                        customer_id = 'fc5f41652a53497e88cdcebc715cc1xz', 
                        enabled = False, 
                        generation = 1627538867363, 
                        https_enabled = True, 
                        https_port = 9997, 
                        id = '8be9321600cbf18e9c8c96bb3217f610', 
                        mem_usage_mi_b = 134, 
                        more_uris = [
                            dscc.models.vasa_uri_info.vasaUriInfo(
                                is_valid = 1, 
                                uri = 'https://xppa6614.in.rdlabs.hpecorp.net:9997/vasa', )
                            ], 
                        server_name = 'xppa6614.in.rdlabs.hpecorp.net', 
                        system_id = '4UW0001540', 
                        system_wwn = '2FF70002AC018D94', 
                        type = 'vasa-settings', 
                        version = '4.0.9.1', ), ),
                request_uri = '/api/v1/storage-systems/device-type1/7CE751P312/network-services/vasa'
            )
        else:
            return NetworkServicesVasa(
        )
        """

    def testNetworkServicesVasa(self):
        """Test NetworkServicesVasa"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
