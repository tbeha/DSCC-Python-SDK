# EncryptionRestoreActionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Encryption key. | [optional] 
**parameters** | [**EncryptionParams**](EncryptionParams.md) |  | [optional] 

## Example

```python
from dscc.models.encryption_restore_action_input import EncryptionRestoreActionInput

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionRestoreActionInput from a JSON string
encryption_restore_action_input_instance = EncryptionRestoreActionInput.from_json(json)
# print the JSON string representation of the object
print(EncryptionRestoreActionInput.to_json())

# convert the object into a dict
encryption_restore_action_input_dict = encryption_restore_action_input_instance.to_dict()
# create an instance of EncryptionRestoreActionInput from a dict
encryption_restore_action_input_from_dict = EncryptionRestoreActionInput.from_dict(encryption_restore_action_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


