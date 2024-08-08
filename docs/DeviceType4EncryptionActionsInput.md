# DeviceType4EncryptionActionsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**DeviceType4EncryptionParams**](DeviceType4EncryptionParams.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_encryption_actions_input import DeviceType4EncryptionActionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EncryptionActionsInput from a JSON string
device_type4_encryption_actions_input_instance = DeviceType4EncryptionActionsInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EncryptionActionsInput.to_json())

# convert the object into a dict
device_type4_encryption_actions_input_dict = device_type4_encryption_actions_input_instance.to_dict()
# create an instance of DeviceType4EncryptionActionsInput from a dict
device_type4_encryption_actions_input_from_dict = DeviceType4EncryptionActionsInput.from_dict(device_type4_encryption_actions_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


