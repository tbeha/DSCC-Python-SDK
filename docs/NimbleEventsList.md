# NimbleEventsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleEventsListItemsInner]**](NimbleEventsListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for Events objects | [optional] 
**total** | **int** | Total number of Events. | [optional] 

## Example

```python
from dscc.models.nimble_events_list import NimbleEventsList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleEventsList from a JSON string
nimble_events_list_instance = NimbleEventsList.from_json(json)
# print the JSON string representation of the object
print(NimbleEventsList.to_json())

# convert the object into a dict
nimble_events_list_dict = nimble_events_list_instance.to_dict()
# create an instance of NimbleEventsList from a dict
nimble_events_list_from_dict = NimbleEventsList.from_dict(nimble_events_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


