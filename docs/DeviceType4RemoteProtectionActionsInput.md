# DeviceType4RemoteProtectionActionsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Actions on the volume set where remote protection is enabled. | [optional] 
**parameters** | [**DeviceType4RemoteProtectionActionsInputParams**](DeviceType4RemoteProtectionActionsInputParams.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_remote_protection_actions_input import DeviceType4RemoteProtectionActionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RemoteProtectionActionsInput from a JSON string
device_type4_remote_protection_actions_input_instance = DeviceType4RemoteProtectionActionsInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RemoteProtectionActionsInput.to_json())

# convert the object into a dict
device_type4_remote_protection_actions_input_dict = device_type4_remote_protection_actions_input_instance.to_dict()
# create an instance of DeviceType4RemoteProtectionActionsInput from a dict
device_type4_remote_protection_actions_input_from_dict = DeviceType4RemoteProtectionActionsInput.from_dict(device_type4_remote_protection_actions_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


