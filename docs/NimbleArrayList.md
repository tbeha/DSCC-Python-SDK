# NimbleArrayList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleArray]**](NimbleArray.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of systems | [optional] 

## Example

```python
from dscc.models.nimble_array_list import NimbleArrayList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleArrayList from a JSON string
nimble_array_list_instance = NimbleArrayList.from_json(json)
# print the JSON string representation of the object
print(NimbleArrayList.to_json())

# convert the object into a dict
nimble_array_list_dict = nimble_array_list_instance.to_dict()
# create an instance of NimbleArrayList from a dict
nimble_array_list_from_dict = NimbleArrayList.from_dict(nimble_array_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


