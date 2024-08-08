# EncryptionActionsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**EncryptionParams**](EncryptionParams.md) |  | [optional] 

## Example

```python
from dscc.models.encryption_actions_input import EncryptionActionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionActionsInput from a JSON string
encryption_actions_input_instance = EncryptionActionsInput.from_json(json)
# print the JSON string representation of the object
print(EncryptionActionsInput.to_json())

# convert the object into a dict
encryption_actions_input_dict = encryption_actions_input_instance.to_dict()
# create an instance of EncryptionActionsInput from a dict
encryption_actions_input_from_dict = EncryptionActionsInput.from_dict(encryption_actions_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


