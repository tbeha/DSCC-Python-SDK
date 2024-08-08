# LocalKeyManagerDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str** | requestUri for detailed local key manager objects | [optional] 
**id** | **str** | Identifier for the local key manager. A 42 digit hexadecimal number. | [optional] 
**name** | **str** | Name of local key manager. | [optional] [default to 'default']
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
from dscc.models.local_key_manager_details import LocalKeyManagerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LocalKeyManagerDetails from a JSON string
local_key_manager_details_instance = LocalKeyManagerDetails.from_json(json)
# print the JSON string representation of the object
print(LocalKeyManagerDetails.to_json())

# convert the object into a dict
local_key_manager_details_dict = local_key_manager_details_instance.to_dict()
# create an instance of LocalKeyManagerDetails from a dict
local_key_manager_details_from_dict = LocalKeyManagerDetails.from_dict(local_key_manager_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


