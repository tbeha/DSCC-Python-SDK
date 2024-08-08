# DeviceType4TelemetryStatus

telemetry status of the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**collection_server** | **str** | Callhome Collection server URL | [optional] 
**connectivity_status** | **str** | Callhome connectivity status. | [optional] 
**connectivity_test_time** | [**DeviceType4TelemetryStatusConnectivityTestTime**](DeviceType4TelemetryStatusConnectivityTestTime.md) |  | [optional] 
**details** | [**List[DeviceType4detailsInner]**](DeviceType4detailsInner.md) |  | [optional] 
**id** | **str** | Unique identifier of the callhome status. | [optional] 
**last_file_sent** | **str** | Last sent file name via callhome. | [optional] 
**last_file_transfer_time** | [**DeviceType4TelemetryStatusLastFileTransferTime**](DeviceType4TelemetryStatusLastFileTransferTime.md) |  | [optional] 
**last_successful_connectivity_test_time** | [**DeviceType4TelemetryStatusLastSuccessfulConnectivityTestTime**](DeviceType4TelemetryStatusLastSuccessfulConnectivityTestTime.md) |  | [optional] 
**proxy_connectivity** | **str** | Proxy connectivity status. | [optional] 
**r_da_configured** | **str** | Callhome transport agent configuration details. | [optional] 
**r_da_status** | **str** | Status of Callhome Transport Agent. | [optional] 
**r_sv_s_status** | **str** | Status of callhome agent. | [optional] 
**r_ts_status** | **str** | Status of Real time scrubber. | [optional] 
**request_uri** | **str** | resourceUri for detailed storage object | [optional] 
**resource_uri** | **str** | resourceUri for detailed storage object | [optional] 
**rolled_up_status** | **str** | Callhome Rolled up status. | [optional] 
**shared_volume_status** | **str** | Shared Volume status | [optional] 
**transfer_status** | **str** | Callhome File Transfer transfer. | [optional] 

## Example

```python
from dscc.models.device_type4_telemetry_status import DeviceType4TelemetryStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4TelemetryStatus from a JSON string
device_type4_telemetry_status_instance = DeviceType4TelemetryStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceType4TelemetryStatus.to_json())

# convert the object into a dict
device_type4_telemetry_status_dict = device_type4_telemetry_status_instance.to_dict()
# create an instance of DeviceType4TelemetryStatus from a dict
device_type4_telemetry_status_from_dict = DeviceType4TelemetryStatus.from_dict(device_type4_telemetry_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


