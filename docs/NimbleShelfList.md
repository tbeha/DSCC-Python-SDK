# NimbleShelfList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleShelfListItemsInner]**](NimbleShelfListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for shelf objects | [optional] 
**total** | **int** | Total number of shelves. | [optional] 

## Example

```python
from dscc.models.nimble_shelf_list import NimbleShelfList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleShelfList from a JSON string
nimble_shelf_list_instance = NimbleShelfList.from_json(json)
# print the JSON string representation of the object
print(NimbleShelfList.to_json())

# convert the object into a dict
nimble_shelf_list_dict = nimble_shelf_list_instance.to_dict()
# create an instance of NimbleShelfList from a dict
nimble_shelf_list_from_dict = NimbleShelfList.from_dict(nimble_shelf_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


