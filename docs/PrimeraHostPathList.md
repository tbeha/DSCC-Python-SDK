# PrimeraHostPathList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PrimeraHostPathListObj]**](PrimeraHostPathListObj.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for primera Hostpath objects | [optional] 
**total** | **int** | Total number of host paths. | [optional] 

## Example

```python
from dscc.models.primera_host_path_list import PrimeraHostPathList

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraHostPathList from a JSON string
primera_host_path_list_instance = PrimeraHostPathList.from_json(json)
# print the JSON string representation of the object
print(PrimeraHostPathList.to_json())

# convert the object into a dict
primera_host_path_list_dict = primera_host_path_list_instance.to_dict()
# create an instance of PrimeraHostPathList from a dict
primera_host_path_list_from_dict = PrimeraHostPathList.from_dict(primera_host_path_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


