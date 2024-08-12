# ExternalKeyManagerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExternalKeyManager]**](ExternalKeyManager.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for external key manager | [optional] 
**total** | **int** | Total number of external key managers. | [optional] 

## Example

```python
from dscc.models.external_key_manager_list import ExternalKeyManagerList

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalKeyManagerList from a JSON string
external_key_manager_list_instance = ExternalKeyManagerList.from_json(json)
# print the JSON string representation of the object
print(ExternalKeyManagerList.to_json())

# convert the object into a dict
external_key_manager_list_dict = external_key_manager_list_instance.to_dict()
# create an instance of ExternalKeyManagerList from a dict
external_key_manager_list_from_dict = ExternalKeyManagerList.from_dict(external_key_manager_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


