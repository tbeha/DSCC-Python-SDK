# NimbleFCSessionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleFCSessionListItemsInner]**](NimbleFCSessionListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for Fibre Channel Session objects | [optional] 
**total** | **int** | Total number of Fibre Channel Sessions. | [optional] 

## Example

```python
from dscc.models.nimble_fc_session_list import NimbleFCSessionList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFCSessionList from a JSON string
nimble_fc_session_list_instance = NimbleFCSessionList.from_json(json)
# print the JSON string representation of the object
print(NimbleFCSessionList.to_json())

# convert the object into a dict
nimble_fc_session_list_dict = nimble_fc_session_list_instance.to_dict()
# create an instance of NimbleFCSessionList from a dict
nimble_fc_session_list_from_dict = NimbleFCSessionList.from_dict(nimble_fc_session_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


