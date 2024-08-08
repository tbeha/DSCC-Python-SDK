# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_vasa import DeviceType4Vasa

class TestDeviceType4Vasa(unittest.TestCase):
    """DeviceType4Vasa unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4Vasa:
        """Test DeviceType4Vasa
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4Vasa`
        """
        model = DeviceType4Vasa()
        if include_optional:
            return DeviceType4Vasa(
                cert_details = [
                    dscc.models.device_type4_cert_details_inner.DeviceType4CertDetails_inner(
                        retain_flag = 'true', 
                        subject = 'VASA CERTIFICATE', 
                        thumbprint = 'afiuqnfiqf', 
                        vc_guid = '0983rhifh9q83rh9', )
                    ],
                cert_mgmt = dscc.models.device_type4_cert_mgmt.DeviceType4CertMgmt(
                    default = 'server', 
                    key = 'VASA_CERTMGMT_MODE-1', ),
                cert_subject = 'Unknown',
                cert_thumbprint = 'Unknown',
                cfg_list = [
                    dscc.models.device_type4_cfg_list_inner.DeviceType4CfgList_inner(
                        key = 'VASA_CPG_MODE-1', 
                        value = 'VASA_CPG_VALUE', )
                    ],
                console_uri = 'data-ops-manager/storage-systems/device-type4/SGH014XGSP/settings/system-settings',
                customer_id = 'fc5f41652a53497e88cdcebc715cc1xz',
                enabled = False,
                generation = 1627538867363,
                https_enabled = True,
                https_port = 9997,
                id = '8be9321600cbf18e9c8c96bb3217f610',
                mem_usage_mi_b = 134,
                more_uris = [
                    dscc.models.device_type4_vasa_uri_info.DeviceType4VasaUriInfo(
                        is_valid = 1, 
                        uri = 'https://xppa6614.in.rdlabs.hpecorp.net:9997/vasa', )
                    ],
                server_name = 'xppa6614.in.rdlabs.hpecorp.net',
                service_status = '',
                system_id = '4UW0001540',
                system_wwn = '2FF70002AC018D94',
                type = 'vasa-settings',
                version = '4.0.9.1'
            )
        else:
            return DeviceType4Vasa(
        )
        """

    def testDeviceType4Vasa(self):
        """Test DeviceType4Vasa"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
