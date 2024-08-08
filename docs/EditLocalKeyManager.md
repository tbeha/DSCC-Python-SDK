# EditLocalKeyManager

Edit Nimble local key manager input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the master key is active or not. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**new_passphrase** | **str** | New passphrase for local key manager. String with size from 8 to 64 printable characters. | [optional] 
**passphrase** | **str** | Existing passphrase  for local key manager. String with size from 8 to 64 printable characters. | [optional] 

## Example

```python
from dscc.models.edit_local_key_manager import EditLocalKeyManager

# TODO update the JSON string below
json = "{}"
# create an instance of EditLocalKeyManager from a JSON string
edit_local_key_manager_instance = EditLocalKeyManager.from_json(json)
# print the JSON string representation of the object
print(EditLocalKeyManager.to_json())

# convert the object into a dict
edit_local_key_manager_dict = edit_local_key_manager_instance.to_dict()
# create an instance of EditLocalKeyManager from a dict
edit_local_key_manager_from_dict = EditLocalKeyManager.from_dict(edit_local_key_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


