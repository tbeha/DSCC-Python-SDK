# DeviceType4TelemetryStatusConnectivityTestTime

Last connectivity test time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds | [optional] 
**tz** | **str** | Time zone name | [optional] 

## Example

```python
from dscc.models.device_type4_telemetry_status_connectivity_test_time import DeviceType4TelemetryStatusConnectivityTestTime

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4TelemetryStatusConnectivityTestTime from a JSON string
device_type4_telemetry_status_connectivity_test_time_instance = DeviceType4TelemetryStatusConnectivityTestTime.from_json(json)
# print the JSON string representation of the object
print(DeviceType4TelemetryStatusConnectivityTestTime.to_json())

# convert the object into a dict
device_type4_telemetry_status_connectivity_test_time_dict = device_type4_telemetry_status_connectivity_test_time_instance.to_dict()
# create an instance of DeviceType4TelemetryStatusConnectivityTestTime from a dict
device_type4_telemetry_status_connectivity_test_time_from_dict = DeviceType4TelemetryStatusConnectivityTestTime.from_dict(device_type4_telemetry_status_connectivity_test_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


