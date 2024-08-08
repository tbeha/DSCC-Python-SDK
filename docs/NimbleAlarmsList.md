# NimbleAlarmsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleAlarmsListItemsInner]**](NimbleAlarmsListItemsInner.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for Alarms objects | [optional] 
**total** | **int** | Total number of Alarms. | [optional] 

## Example

```python
from dscc.models.nimble_alarms_list import NimbleAlarmsList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleAlarmsList from a JSON string
nimble_alarms_list_instance = NimbleAlarmsList.from_json(json)
# print the JSON string representation of the object
print(NimbleAlarmsList.to_json())

# convert the object into a dict
nimble_alarms_list_dict = nimble_alarms_list_instance.to_dict()
# create an instance of NimbleAlarmsList from a dict
nimble_alarms_list_from_dict = NimbleAlarmsList.from_dict(nimble_alarms_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


