# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.remote_protection_actions_input import RemoteProtectionActionsInput

class TestRemoteProtectionActionsInput(unittest.TestCase):
    """RemoteProtectionActionsInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemoteProtectionActionsInput:
        """Test RemoteProtectionActionsInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RemoteProtectionActionsInput`
        """
        model = RemoteProtectionActionsInput()
        if include_optional:
            return RemoteProtectionActionsInput(
                action = 'SYNC',
                parameters = dscc.models.remote_protection_actions_input_params.RemoteProtectionActionsInputParams(
                    failover_action_params = dscc.models.failover_params.FailoverParams(
                        discard_new_data = True, 
                        force_pp_failover = True, 
                        no_snapshot = True, 
                        skip_promote = True, 
                        skip_start = True, 
                        skip_sync = True, 
                        target_name = 's1511', ), 
                    override_action_params = dscc.models.override_params.OverrideParams(
                        target_name = 's1511', ), 
                    recover_action_params = dscc.models.recover_params.RecoverParams(
                        skip_start = True, 
                        skip_sync = True, 
                        target_name = 's1511', ), 
                    restore_action_params = dscc.models.restore_params.RestoreParams(
                        no_snapshot = True, 
                        skip_start = True, 
                        skip_sync = True, 
                        target_name = 's1511', ), 
                    reverse_action_params = dscc.models.reverse_params.ReverseParams(
                        current = True, 
                        local_group_direction = True, 
                        natural = True, 
                        no_snapshot = True, 
                        skip_promote = True, 
                        stop_groups = True, 
                        target_name = 's1511', ), 
                    start_action_params = dscc.models.start_params.StartParams(
                        skip_initial_sync = True, 
                        target_name = 's1511', ), 
                    stop_action_params = dscc.models.stop_params.StopParams(
                        no_snapshot = True, 
                        target_name = 's1511', ), 
                    switchover_action_params = dscc.models.switch_over_params.SwitchOverParams(
                        target_name = 's1511', ), 
                    sync_action_params = dscc.models.sync_params.SyncParams(
                        force_full_sync = False, 
                        not_save_resync_snap = False, 
                        target_name = 's1511', ), )
            )
        else:
            return RemoteProtectionActionsInput(
        )
        """

    def testRemoteProtectionActionsInput(self):
        """Test RemoteProtectionActionsInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
