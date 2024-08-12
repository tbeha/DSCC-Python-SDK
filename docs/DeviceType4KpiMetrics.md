# DeviceType4KpiMetrics

kpi metrics with read, write and total average values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | [**DeviceType4pmPerfData**](DeviceType4pmPerfData.md) |  | [optional] 
**total** | [**DeviceType4pmPerfData**](DeviceType4pmPerfData.md) |  | [optional] 
**write** | [**DeviceType4pmPerfData**](DeviceType4pmPerfData.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_kpi_metrics import DeviceType4KpiMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4KpiMetrics from a JSON string
device_type4_kpi_metrics_instance = DeviceType4KpiMetrics.from_json(json)
# print the JSON string representation of the object
print(DeviceType4KpiMetrics.to_json())

# convert the object into a dict
device_type4_kpi_metrics_dict = device_type4_kpi_metrics_instance.to_dict()
# create an instance of DeviceType4KpiMetrics from a dict
device_type4_kpi_metrics_from_dict = DeviceType4KpiMetrics.from_dict(device_type4_kpi_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


