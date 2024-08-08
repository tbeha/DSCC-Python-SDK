# NimblePoolsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimblePoolsListItemsInner]**](NimblePoolsListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for storage pool objects | [optional] 
**total** | **int** | Total number of pools. | [optional] 

## Example

```python
from dscc.models.nimble_pools_list import NimblePoolsList

# TODO update the JSON string below
json = "{}"
# create an instance of NimblePoolsList from a JSON string
nimble_pools_list_instance = NimblePoolsList.from_json(json)
# print the JSON string representation of the object
print(NimblePoolsList.to_json())

# convert the object into a dict
nimble_pools_list_dict = nimble_pools_list_instance.to_dict()
# create an instance of NimblePoolsList from a dict
nimble_pools_list_from_dict = NimblePoolsList.from_dict(nimble_pools_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


