# PrimeraStorageSystemList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PrimeraStorageSystemDetailList]**](PrimeraStorageSystemDetailList.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**total** | **int** | Number of systems | [optional] 

## Example

```python
from dscc.models.primera_storage_system_list import PrimeraStorageSystemList

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraStorageSystemList from a JSON string
primera_storage_system_list_instance = PrimeraStorageSystemList.from_json(json)
# print the JSON string representation of the object
print(PrimeraStorageSystemList.to_json())

# convert the object into a dict
primera_storage_system_list_dict = primera_storage_system_list_instance.to_dict()
# create an instance of PrimeraStorageSystemList from a dict
primera_storage_system_list_from_dict = PrimeraStorageSystemList.from_dict(primera_storage_system_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


