# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4snmp_details import DeviceType4snmpDetails

class TestDeviceType4snmpDetails(unittest.TestCase):
    """DeviceType4snmpDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4snmpDetails:
        """Test DeviceType4snmpDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4snmpDetails`
        """
        model = DeviceType4snmpDetails()
        if include_optional:
            return DeviceType4snmpDetails(
                items = [
                    dscc.models.device_type4snmp.DeviceType4snmp(
                        console_uri = 'data-ops-manager/storage-systems/device-type4/SGH014XGSP/settings/system-settings', 
                        customer_id = 'fc5f41652a53497e88cdcebc715cc1fg', 
                        generation = 1627533045690, 
                        id = '8be9321600cbf18e9c8c96bb3217f610', 
                        manager_ip = '15.218.169.163', 
                        notify = 'STANDARD', 
                        port = 162, 
                        system_id = '4UW0001540', 
                        system_wwn = '2FF70002AC018D94', 
                        type = 'snmp-manager-settings', 
                        user = 'user1', 
                        version = 2, )
                    ],
                page_limit = 1,
                page_offset = 1,
                total = 1
            )
        else:
            return DeviceType4snmpDetails(
        )
        """

    def testDeviceType4snmpDetails(self):
        """Test DeviceType4snmpDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
