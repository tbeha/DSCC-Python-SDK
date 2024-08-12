# DeviceType4Schedule

Schedule created on application set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at_time** | **int** | Time of the day when snapshot should be taken. If more than one snapshots in a day then untilTime specifies until what time snapshots should be taken | [optional] 
**customer_id** | **str** | tenantId of resource | [optional] 
**day_of_month** | **int** | Day of month that a scheduled task will execute. Allowed values are 1-28 | [optional] 
**days** | **str** | Days on which schedule task will run. Possible values: sunday,monday,tuesday,wednesday,thursday,friday,saturday | [optional] 
**expire_secs** | **int** | Expiration time in seconds | [optional] 
**generation** | **int** | Generation value | [optional] 
**id** | **str** | Unique Identifier of the resource | [optional] 
**is_alert_enabled** | **bool** | Whether the schedule will generate an alert if it could not run. | [optional] 
**is_paused** | **bool** | Whether the schedule has been paused. | [optional] 
**is_remote** | **bool** | Specifies that this schedule is remote protection schedule | [optional] 
**is_system_task** | **bool** | Whether the schedule is a system created one. | [optional] 
**name** | **str** | Name of the resource | [optional] 
**next_run_time** | **int** | The next time a schedule will run | [optional] 
**period** | **int** | Time interval for schedule task to run. Possible values:               - hours: 1,2,3,4,6,8,12               - minutes: 15,20,30               - days &amp; months: 1 | [optional] 
**period_unit** | **str** | Unit of time in which period is defined. Possible values: minutes, hours, days, months | [optional] 
**retain_secs** | **int** | Retention time in seconds. | [optional] 
**status** | **str** | Whether the schedule task is active or has been suspended | [optional] 
**system_wwn** | **str** | WWN of the array | [optional] 
**type** | **str** | Type of object | [optional] 
**until_time** | **int** | Time of the day to stop taking snapshots. Applicable only when more than one snapshots should be taken in a day. | [optional] 
**user** | **str** | The user that created the schedule. | [optional] 

## Example

```python
from dscc.models.device_type4_schedule import DeviceType4Schedule

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4Schedule from a JSON string
device_type4_schedule_instance = DeviceType4Schedule.from_json(json)
# print the JSON string representation of the object
print(DeviceType4Schedule.to_json())

# convert the object into a dict
device_type4_schedule_dict = device_type4_schedule_instance.to_dict()
# create an instance of DeviceType4Schedule from a dict
device_type4_schedule_from_dict = DeviceType4Schedule.from_dict(device_type4_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


