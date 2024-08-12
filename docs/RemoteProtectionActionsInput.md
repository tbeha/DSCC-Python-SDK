# RemoteProtectionActionsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Actions on the volume set where remote protection is enabled. | [optional] 
**parameters** | [**RemoteProtectionActionsInputParams**](RemoteProtectionActionsInputParams.md) |  | [optional] 

## Example

```python
from dscc.models.remote_protection_actions_input import RemoteProtectionActionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteProtectionActionsInput from a JSON string
remote_protection_actions_input_instance = RemoteProtectionActionsInput.from_json(json)
# print the JSON string representation of the object
print(RemoteProtectionActionsInput.to_json())

# convert the object into a dict
remote_protection_actions_input_dict = remote_protection_actions_input_instance.to_dict()
# create an instance of RemoteProtectionActionsInput from a dict
remote_protection_actions_input_from_dict = RemoteProtectionActionsInput.from_dict(remote_protection_actions_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


