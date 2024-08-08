# DeviceType4EncryptionRestoreActionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Encryption key. | [optional] 
**parameters** | [**DeviceType4EncryptionBackupRekeyRestoreParams**](DeviceType4EncryptionBackupRekeyRestoreParams.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_encryption_restore_action_input import DeviceType4EncryptionRestoreActionInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EncryptionRestoreActionInput from a JSON string
device_type4_encryption_restore_action_input_instance = DeviceType4EncryptionRestoreActionInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EncryptionRestoreActionInput.to_json())

# convert the object into a dict
device_type4_encryption_restore_action_input_dict = device_type4_encryption_restore_action_input_instance.to_dict()
# create an instance of DeviceType4EncryptionRestoreActionInput from a dict
device_type4_encryption_restore_action_input_from_dict = DeviceType4EncryptionRestoreActionInput.from_dict(device_type4_encryption_restore_action_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


