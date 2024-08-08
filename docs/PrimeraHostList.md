# PrimeraHostList

List of primera Host Paths

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PrimeraHostListObj]**](PrimeraHostListObj.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**total** | **int** | Total number of Hosts | [optional] 

## Example

```python
from dscc.models.primera_host_list import PrimeraHostList

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraHostList from a JSON string
primera_host_list_instance = PrimeraHostList.from_json(json)
# print the JSON string representation of the object
print(PrimeraHostList.to_json())

# convert the object into a dict
primera_host_list_dict = primera_host_list_instance.to_dict()
# create an instance of PrimeraHostList from a dict
primera_host_list_from_dict = PrimeraHostList.from_dict(primera_host_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


