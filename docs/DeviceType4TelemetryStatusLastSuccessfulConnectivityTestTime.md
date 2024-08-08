# DeviceType4TelemetryStatusLastSuccessfulConnectivityTestTime

Last successful connectivity time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds | [optional] 
**tz** | **str** | Time zone name | [optional] 

## Example

```python
from dscc.models.device_type4_telemetry_status_last_successful_connectivity_test_time import DeviceType4TelemetryStatusLastSuccessfulConnectivityTestTime

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4TelemetryStatusLastSuccessfulConnectivityTestTime from a JSON string
device_type4_telemetry_status_last_successful_connectivity_test_time_instance = DeviceType4TelemetryStatusLastSuccessfulConnectivityTestTime.from_json(json)
# print the JSON string representation of the object
print(DeviceType4TelemetryStatusLastSuccessfulConnectivityTestTime.to_json())

# convert the object into a dict
device_type4_telemetry_status_last_successful_connectivity_test_time_dict = device_type4_telemetry_status_last_successful_connectivity_test_time_instance.to_dict()
# create an instance of DeviceType4TelemetryStatusLastSuccessfulConnectivityTestTime from a dict
device_type4_telemetry_status_last_successful_connectivity_test_time_from_dict = DeviceType4TelemetryStatusLastSuccessfulConnectivityTestTime.from_dict(device_type4_telemetry_status_last_successful_connectivity_test_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


