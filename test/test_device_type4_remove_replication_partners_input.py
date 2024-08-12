# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_remove_replication_partners_input import DeviceType4RemoveReplicationPartnersInput

class TestDeviceType4RemoveReplicationPartnersInput(unittest.TestCase):
    """DeviceType4RemoveReplicationPartnersInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4RemoveReplicationPartnersInput:
        """Test DeviceType4RemoveReplicationPartnersInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4RemoveReplicationPartnersInput`
        """
        model = DeviceType4RemoveReplicationPartnersInput()
        if include_optional:
            return DeviceType4RemoveReplicationPartnersInput(
                replication_partners = [
                    dscc.models.device_type4_remove_remote_copy_target_input.DeviceType4RemoveRemoteCopyTargetInput(
                        replication_partner_system_id = '7CE816P0SR', 
                        src_replication_id = 'afb4961e47212e5bc88dd35db5be5c83', 
                        target_replication_id = 'afb4961e47212e5bc88dd35db5be5c83', )
                    ]
            )
        else:
            return DeviceType4RemoveReplicationPartnersInput(
                replication_partners = [
                    dscc.models.device_type4_remove_remote_copy_target_input.DeviceType4RemoveRemoteCopyTargetInput(
                        replication_partner_system_id = '7CE816P0SR', 
                        src_replication_id = 'afb4961e47212e5bc88dd35db5be5c83', 
                        target_replication_id = 'afb4961e47212e5bc88dd35db5be5c83', )
                    ],
        )
        """

    def testDeviceType4RemoveReplicationPartnersInput(self):
        """Test DeviceType4RemoveReplicationPartnersInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
