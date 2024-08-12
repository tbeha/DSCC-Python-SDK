# CalendarTime

Time zone and epoch time

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds | [optional] 
**tz** | **str** | Time zone name | [optional] 

## Example

```python
from dscc.models.calendar_time import CalendarTime

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarTime from a JSON string
calendar_time_instance = CalendarTime.from_json(json)
# print the JSON string representation of the object
print(CalendarTime.to_json())

# convert the object into a dict
calendar_time_dict = calendar_time_instance.to_dict()
# create an instance of CalendarTime from a dict
calendar_time_from_dict = CalendarTime.from_dict(calendar_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


