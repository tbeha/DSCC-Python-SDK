# DeviceType4ProtectionScheduleInputSchema

Protection schedule details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at_time** | **int** | Time of the day when snapshot should be taken. Possible values: 0-23 If more than one snapshots in a day then untilTime specifies until what time snapshots should be taken. | [optional] 
**day_of_month** | **int** | Day of month on which snapshot has to be taken for Monthly schedule. Possible values: 1-28 | [optional] 
**days** | **str** | Days on which snapshots should be taken. comma separated. Possible values: sunday,monday,tuesday,wednesday,thursday,friday,saturday | [optional] 
**expire_secs** | **int** | Number of seconds the snapshot has to be retained. | 
**is_remote** | **bool** | Specifies that this schedule is remote protection schedule | 
**name** | **str** | Name of the Schedule | 
**period** | **int** | Time interval for snapshots. Possible values:   - hours: 1,2,3,4,6,8,12   - minutes: 15,20,30   - days &amp; months: 1 | 
**period_unit** | **str** | Unit of time for the interval specified in period. | 
**retain_secs** | **int** | Specifies the amount of time in seconds, relative to the current time, that the snapshot will be retained. It is a positive integer value and in the range of 1 hour - 1825 days. If both expiration time and retention time are specified, then the retention time cannot be longer than the expiration time. | [optional] 
**until_time** | **int** | Time of the day to stop taking snapshots. Must be an incremental value by the factor specified in Period, starting from atTime. Applicable only when more than one snapshots should be taken in a day. | [optional] 

## Example

```python
from dscc.models.device_type4_protection_schedule_input_schema import DeviceType4ProtectionScheduleInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ProtectionScheduleInputSchema from a JSON string
device_type4_protection_schedule_input_schema_instance = DeviceType4ProtectionScheduleInputSchema.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ProtectionScheduleInputSchema.to_json())

# convert the object into a dict
device_type4_protection_schedule_input_schema_dict = device_type4_protection_schedule_input_schema_instance.to_dict()
# create an instance of DeviceType4ProtectionScheduleInputSchema from a dict
device_type4_protection_schedule_input_schema_from_dict = DeviceType4ProtectionScheduleInputSchema.from_dict(device_type4_protection_schedule_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


