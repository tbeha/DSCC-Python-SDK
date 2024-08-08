# PrimeraHostSetList

List of primera Host Paths

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PrimeraHostSetListObj]**](PrimeraHostSetListObj.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**total** | **int** | Number of hostsets | [optional] 

## Example

```python
from dscc.models.primera_host_set_list import PrimeraHostSetList

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraHostSetList from a JSON string
primera_host_set_list_instance = PrimeraHostSetList.from_json(json)
# print the JSON string representation of the object
print(PrimeraHostSetList.to_json())

# convert the object into a dict
primera_host_set_list_dict = primera_host_set_list_instance.to_dict()
# create an instance of PrimeraHostSetList from a dict
primera_host_set_list_from_dict = PrimeraHostSetList.from_dict(primera_host_set_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


