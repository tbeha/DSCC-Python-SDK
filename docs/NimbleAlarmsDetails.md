# NimbleAlarmsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | **str** | Description of the alarms. String of 1-1476 printable characters. | [optional] 
**alarm_type** | **int** | Identifier for type of alarm. Non-negative integer in range [0,2147483647]. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**summary** | **str** | Summary of the alarm. Plain string. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.nimble_alarms_details import NimbleAlarmsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleAlarmsDetails from a JSON string
nimble_alarms_details_instance = NimbleAlarmsDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleAlarmsDetails.to_json())

# convert the object into a dict
nimble_alarms_details_dict = nimble_alarms_details_instance.to_dict()
# create an instance of NimbleAlarmsDetails from a dict
nimble_alarms_details_from_dict = NimbleAlarmsDetails.from_dict(nimble_alarms_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


