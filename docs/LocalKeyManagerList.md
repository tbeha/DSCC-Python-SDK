# LocalKeyManagerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[LocalKeyManager]**](LocalKeyManager.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for local key manager | [optional] 
**total** | **int** | Total number of local key managers. | [optional] 

## Example

```python
from dscc.models.local_key_manager_list import LocalKeyManagerList

# TODO update the JSON string below
json = "{}"
# create an instance of LocalKeyManagerList from a JSON string
local_key_manager_list_instance = LocalKeyManagerList.from_json(json)
# print the JSON string representation of the object
print(LocalKeyManagerList.to_json())

# convert the object into a dict
local_key_manager_list_dict = local_key_manager_list_instance.to_dict()
# create an instance of LocalKeyManagerList from a dict
local_key_manager_list_from_dict = LocalKeyManagerList.from_dict(local_key_manager_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


