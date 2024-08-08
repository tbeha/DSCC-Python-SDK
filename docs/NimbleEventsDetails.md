# NimbleEventsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | **str** | Description of the event. String of 1-1476 printable characters. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**summary** | **str** | Summary of the event. Plain string. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.nimble_events_details import NimbleEventsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleEventsDetails from a JSON string
nimble_events_details_instance = NimbleEventsDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleEventsDetails.to_json())

# convert the object into a dict
nimble_events_details_dict = nimble_events_details_instance.to_dict()
# create an instance of NimbleEventsDetails from a dict
nimble_events_details_from_dict = NimbleEventsDetails.from_dict(nimble_events_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


