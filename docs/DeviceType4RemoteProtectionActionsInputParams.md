# DeviceType4RemoteProtectionActionsInputParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_action_params** | [**DeviceType4FailoverParams**](DeviceType4FailoverParams.md) |  | [optional] 
**override_action_params** | [**DeviceType4OverrideParams**](DeviceType4OverrideParams.md) |  | [optional] 
**recover_action_params** | [**DeviceType4RecoverParams**](DeviceType4RecoverParams.md) |  | [optional] 
**restore_action_params** | [**DeviceType4RestoreParams**](DeviceType4RestoreParams.md) |  | [optional] 
**reverse_action_params** | [**DeviceType4ReverseParams**](DeviceType4ReverseParams.md) |  | [optional] 
**start_action_params** | [**DeviceType4StartParams**](DeviceType4StartParams.md) |  | [optional] 
**stop_action_params** | [**DeviceType4StopParams**](DeviceType4StopParams.md) |  | [optional] 
**switchover_action_params** | [**DeviceType4SwitchOverParams**](DeviceType4SwitchOverParams.md) |  | [optional] 
**sync_action_params** | [**DeviceType4SyncParams**](DeviceType4SyncParams.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_remote_protection_actions_input_params import DeviceType4RemoteProtectionActionsInputParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RemoteProtectionActionsInputParams from a JSON string
device_type4_remote_protection_actions_input_params_instance = DeviceType4RemoteProtectionActionsInputParams.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RemoteProtectionActionsInputParams.to_json())

# convert the object into a dict
device_type4_remote_protection_actions_input_params_dict = device_type4_remote_protection_actions_input_params_instance.to_dict()
# create an instance of DeviceType4RemoteProtectionActionsInputParams from a dict
device_type4_remote_protection_actions_input_params_from_dict = DeviceType4RemoteProtectionActionsInputParams.from_dict(device_type4_remote_protection_actions_input_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


