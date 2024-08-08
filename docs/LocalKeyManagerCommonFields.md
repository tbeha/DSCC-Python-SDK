# LocalKeyManagerCommonFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates if the local key manager is active or not | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**purge_age** | **int** | Default minimum age (in hours) of inactive encryption keys to be purged. &#39;0&#39; indicates to purge keys immediately. Signed 64-bit integer. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.local_key_manager_common_fields import LocalKeyManagerCommonFields

# TODO update the JSON string below
json = "{}"
# create an instance of LocalKeyManagerCommonFields from a JSON string
local_key_manager_common_fields_instance = LocalKeyManagerCommonFields.from_json(json)
# print the JSON string representation of the object
print(LocalKeyManagerCommonFields.to_json())

# convert the object into a dict
local_key_manager_common_fields_dict = local_key_manager_common_fields_instance.to_dict()
# create an instance of LocalKeyManagerCommonFields from a dict
local_key_manager_common_fields_from_dict = LocalKeyManagerCommonFields.from_dict(local_key_manager_common_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


