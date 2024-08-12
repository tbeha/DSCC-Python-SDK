# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_witness_common import DeviceType4WitnessCommon

class TestDeviceType4WitnessCommon(unittest.TestCase):
    """DeviceType4WitnessCommon unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4WitnessCommon:
        """Test DeviceType4WitnessCommon
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4WitnessCommon`
        """
        model = DeviceType4WitnessCommon()
        if include_optional:
            return DeviceType4WitnessCommon(
                associated_links = [{"link":"/v1/storage-systems/SGH000XWEE","type":"systems"}],
                common_resource_attributes = dscc.models.common_resource_attributes.commonResourceAttributes(
                    cloud_state = 'CONNECTED', ),
                customer_id = 'fc5f41652a53497e88cdcebc715cc1cf',
                generation = 0,
                is_remote_array_support_replication = True,
                name = 'IPSource',
                quorum_atf_timeout = 30,
                quorum_ip_address = '10.10.10.11',
                quorum_ssl_port = 8843,
                quorum_status = 'Initializing',
                quorum_status_qual = 'NA',
                quorum_version = '2.0',
                remote_id = '6a5ce66d4814a5e5156de428abb0a580',
                remote_name = 'IPTarget',
                remote_system_id = 'SGH000XWEF',
                remote_system_name = 'System102',
                resource_uri = '/api/v1/storage-systems/device-type4/SGH000XWEE/system-settings/quorum-witness/5a5ce66d4814a5e5156de428abb0a589',
                system_id = 'SGH000XWEE',
                system_name = 's1511',
                type = 'quorum-witness'
            )
        else:
            return DeviceType4WitnessCommon(
        )
        """

    def testDeviceType4WitnessCommon(self):
        """Test DeviceType4WitnessCommon"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
