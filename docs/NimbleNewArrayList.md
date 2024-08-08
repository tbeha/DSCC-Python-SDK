# NimbleNewArrayList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleNewArrayListItemsInner]**](NimbleNewArrayListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of systems | [optional] 

## Example

```python
from dscc.models.nimble_new_array_list import NimbleNewArrayList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleNewArrayList from a JSON string
nimble_new_array_list_instance = NimbleNewArrayList.from_json(json)
# print the JSON string representation of the object
print(NimbleNewArrayList.to_json())

# convert the object into a dict
nimble_new_array_list_dict = nimble_new_array_list_instance.to_dict()
# create an instance of NimbleNewArrayList from a dict
nimble_new_array_list_from_dict = NimbleNewArrayList.from_dict(nimble_new_array_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


