# NimbleControllerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleControllerListItemsInner]**](NimbleControllerListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for controller objects | [optional] 
**total** | **int** | Total number of controllers. | [optional] 

## Example

```python
from dscc.models.nimble_controller_list import NimbleControllerList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleControllerList from a JSON string
nimble_controller_list_instance = NimbleControllerList.from_json(json)
# print the JSON string representation of the object
print(NimbleControllerList.to_json())

# convert the object into a dict
nimble_controller_list_dict = nimble_controller_list_instance.to_dict()
# create an instance of NimbleControllerList from a dict
nimble_controller_list_from_dict = NimbleControllerList.from_dict(nimble_controller_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


