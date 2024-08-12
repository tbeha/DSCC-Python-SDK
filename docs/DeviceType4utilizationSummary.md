# DeviceType4utilizationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_usage_data** | [**DeviceType4utilizationSummaryCapacityUsageData**](DeviceType4utilizationSummaryCapacityUsageData.md) |  | [optional] 
**provisioned_capacity** | **float** | Provisioned capacity | [optional] 

## Example

```python
from dscc.models.device_type4utilization_summary import DeviceType4utilizationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4utilizationSummary from a JSON string
device_type4utilization_summary_instance = DeviceType4utilizationSummary.from_json(json)
# print the JSON string representation of the object
print(DeviceType4utilizationSummary.to_json())

# convert the object into a dict
device_type4utilization_summary_dict = device_type4utilization_summary_instance.to_dict()
# create an instance of DeviceType4utilizationSummary from a dict
device_type4utilization_summary_from_dict = DeviceType4utilizationSummary.from_dict(device_type4utilization_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


