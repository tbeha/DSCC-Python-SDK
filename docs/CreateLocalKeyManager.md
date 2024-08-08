# CreateLocalKeyManager

Create local key manager input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passphrase** | **str** | Passphrase  for local key manager. String with size from 8 to 64 printable characters. | 

## Example

```python
from dscc.models.create_local_key_manager import CreateLocalKeyManager

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLocalKeyManager from a JSON string
create_local_key_manager_instance = CreateLocalKeyManager.from_json(json)
# print the JSON string representation of the object
print(CreateLocalKeyManager.to_json())

# convert the object into a dict
create_local_key_manager_dict = create_local_key_manager_instance.to_dict()
# create an instance of CreateLocalKeyManager from a dict
create_local_key_manager_from_dict = CreateLocalKeyManager.from_dict(create_local_key_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


