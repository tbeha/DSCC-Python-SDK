# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_network_services_cim import DeviceType4NetworkServicesCim

class TestDeviceType4NetworkServicesCim(unittest.TestCase):
    """DeviceType4NetworkServicesCim unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4NetworkServicesCim:
        """Test DeviceType4NetworkServicesCim
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4NetworkServicesCim`
        """
        model = DeviceType4NetworkServicesCim()
        if include_optional:
            return DeviceType4NetworkServicesCim(
                items = dscc.models.device_type4cim_details.DeviceType4cimDetails(
                    associated_links = [{"resourceUri":"/api/v1/storage-systems/device-type4/{uid}","type":"systems"}], 
                    cim = dscc.models.device_type4cim.DeviceType4cim(
                        cim_policy = 'replica_entity,one_hwid_per_view,use_pegasus_interop_namespace,no_tls_strict', 
                        cim_state = 'Active', 
                        cim_version = 'V1', 
                        console_uri = 'data-ops-manager/storage-systems/device-type4/SGH014XGSP/settings/system-settings', 
                        customer_id = 'fc5f41652a53497e88cdcebc715cc1qw', 
                        generation = 1627533171477, 
                        http_port = 5988, 
                        http_state = False, 
                        https_port = 5989, 
                        https_state = True, 
                        id = '012e5dce5c029c4c56bdda9b3e1eaaad', 
                        pg_version = '2.14.1', 
                        service_state = True, 
                        slp_port = 427, 
                        slp_state = True, 
                        system_id = '4UW0001540', 
                        system_wwn = '2FF70002AC018D94', 
                        type = 'cim-settings', ), 
                    common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                        cloud_state = 'CONNECTED', ), 
                    system_id = '4UW0001540', ),
                request_uri = '/api/v1/storage-systems/device-type4/7CE751P312/network-services/cim'
            )
        else:
            return DeviceType4NetworkServicesCim(
        )
        """

    def testDeviceType4NetworkServicesCim(self):
        """Test DeviceType4NetworkServicesCim"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
