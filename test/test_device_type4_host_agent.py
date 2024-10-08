# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_host_agent import DeviceType4HostAgent

class TestDeviceType4HostAgent(unittest.TestCase):
    """DeviceType4HostAgent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4HostAgent:
        """Test DeviceType4HostAgent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4HostAgent`
        """
        model = DeviceType4HostAgent()
        if include_optional:
            return DeviceType4HostAgent(
                ip_addr = '10.15.12.136',
                architecture = 'SAN',
                boot_from_san = 'yes',
                cluster_id = '113245',
                cluster_name = 'SAN-cluster',
                cluster_software = 'Linux',
                cluster_version = 'v1.0.0',
                host_apps = 'mysql',
                last_updated = dscc.models.device_type4_host_agent_last_updated.DeviceType4HostAgent_lastUpdated(
                    ms = 101780, 
                    tz = '123545', ),
                multi_path_software = 'OS',
                multi_path_software_version = 'v1.0.0',
                os = 'Linux',
                os_patch = 'v1.0.0',
                os_version = 'v1.0.0',
                reported_name = 'slvs'
            )
        else:
            return DeviceType4HostAgent(
        )
        """

    def testDeviceType4HostAgent(self):
        """Test DeviceType4HostAgent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
