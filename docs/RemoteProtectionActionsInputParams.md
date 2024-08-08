# RemoteProtectionActionsInputParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_action_params** | [**FailoverParams**](FailoverParams.md) |  | [optional] 
**override_action_params** | [**OverrideParams**](OverrideParams.md) |  | [optional] 
**recover_action_params** | [**RecoverParams**](RecoverParams.md) |  | [optional] 
**restore_action_params** | [**RestoreParams**](RestoreParams.md) |  | [optional] 
**reverse_action_params** | [**ReverseParams**](ReverseParams.md) |  | [optional] 
**start_action_params** | [**StartParams**](StartParams.md) |  | [optional] 
**stop_action_params** | [**StopParams**](StopParams.md) |  | [optional] 
**switchover_action_params** | [**SwitchOverParams**](SwitchOverParams.md) |  | [optional] 
**sync_action_params** | [**SyncParams**](SyncParams.md) |  | [optional] 

## Example

```python
from dscc.models.remote_protection_actions_input_params import RemoteProtectionActionsInputParams

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteProtectionActionsInputParams from a JSON string
remote_protection_actions_input_params_instance = RemoteProtectionActionsInputParams.from_json(json)
# print the JSON string representation of the object
print(RemoteProtectionActionsInputParams.to_json())

# convert the object into a dict
remote_protection_actions_input_params_dict = remote_protection_actions_input_params_instance.to_dict()
# create an instance of RemoteProtectionActionsInputParams from a dict
remote_protection_actions_input_params_from_dict = RemoteProtectionActionsInputParams.from_dict(remote_protection_actions_input_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


