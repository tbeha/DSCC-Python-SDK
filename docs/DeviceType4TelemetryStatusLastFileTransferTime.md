# DeviceType4TelemetryStatusLastFileTransferTime

Last sent file time via callhome.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds | [optional] 
**tz** | **str** | Time zone name | [optional] 

## Example

```python
from dscc.models.device_type4_telemetry_status_last_file_transfer_time import DeviceType4TelemetryStatusLastFileTransferTime

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4TelemetryStatusLastFileTransferTime from a JSON string
device_type4_telemetry_status_last_file_transfer_time_instance = DeviceType4TelemetryStatusLastFileTransferTime.from_json(json)
# print the JSON string representation of the object
print(DeviceType4TelemetryStatusLastFileTransferTime.to_json())

# convert the object into a dict
device_type4_telemetry_status_last_file_transfer_time_dict = device_type4_telemetry_status_last_file_transfer_time_instance.to_dict()
# create an instance of DeviceType4TelemetryStatusLastFileTransferTime from a dict
device_type4_telemetry_status_last_file_transfer_time_from_dict = DeviceType4TelemetryStatusLastFileTransferTime.from_dict(device_type4_telemetry_status_last_file_transfer_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


