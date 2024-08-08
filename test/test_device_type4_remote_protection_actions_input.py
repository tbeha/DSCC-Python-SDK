# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.device_type4_remote_protection_actions_input import DeviceType4RemoteProtectionActionsInput

class TestDeviceType4RemoteProtectionActionsInput(unittest.TestCase):
    """DeviceType4RemoteProtectionActionsInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceType4RemoteProtectionActionsInput:
        """Test DeviceType4RemoteProtectionActionsInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceType4RemoteProtectionActionsInput`
        """
        model = DeviceType4RemoteProtectionActionsInput()
        if include_optional:
            return DeviceType4RemoteProtectionActionsInput(
                action = 'SYNC',
                parameters = dscc.models.device_type4_remote_protection_actions_input_params.DeviceType4RemoteProtectionActionsInputParams(
                    failover_action_params = dscc.models.device_type4_failover_params.DeviceType4FailoverParams(
                        force_pp_failover = True, 
                        no_snapshot = True, 
                        skip_promote = True, 
                        target_name = 's1511', ), 
                    override_action_params = dscc.models.device_type4_override_params.DeviceType4OverrideParams(
                        target_name = 's1511', ), 
                    recover_action_params = dscc.models.device_type4_recover_params.DeviceType4RecoverParams(
                        skip_start = True, 
                        skip_sync = True, 
                        target_name = 's1511', ), 
                    restore_action_params = dscc.models.device_type4_restore_params.DeviceType4RestoreParams(
                        no_snapshot = True, 
                        skip_start = True, 
                        skip_sync = True, 
                        target_name = 's1511', ), 
                    reverse_action_params = dscc.models.device_type4_reverse_params.DeviceType4ReverseParams(
                        current = True, 
                        local_group_direction = True, 
                        natural = True, 
                        no_snapshot = True, 
                        skip_promote = True, 
                        stop_groups = True, 
                        target_name = 's1511', ), 
                    start_action_params = dscc.models.device_type4_start_params.DeviceType4StartParams(
                        target_name = 's1511', ), 
                    stop_action_params = dscc.models.device_type4_stop_params.DeviceType4StopParams(
                        target_name = 's1511', ), 
                    switchover_action_params = dscc.models.device_type4_switch_over_params.DeviceType4SwitchOverParams(
                        no_snapshot = False, 
                        target_name = 's1511', ), 
                    sync_action_params = dscc.models.device_type4_sync_params.DeviceType4SyncParams(
                        force_full_sync = False, ), )
            )
        else:
            return DeviceType4RemoteProtectionActionsInput(
        )
        """

    def testDeviceType4RemoteProtectionActionsInput(self):
        """Test DeviceType4RemoteProtectionActionsInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
