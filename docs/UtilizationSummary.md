# UtilizationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_usage_data** | [**DeviceType4utilizationSummaryCapacityUsageData**](DeviceType4utilizationSummaryCapacityUsageData.md) |  | [optional] 
**provisioned_capacity** | **float** | Provisioned capacity | [optional] 

## Example

```python
from dscc.models.utilization_summary import UtilizationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of UtilizationSummary from a JSON string
utilization_summary_instance = UtilizationSummary.from_json(json)
# print the JSON string representation of the object
print(UtilizationSummary.to_json())

# convert the object into a dict
utilization_summary_dict = utilization_summary_instance.to_dict()
# create an instance of UtilizationSummary from a dict
utilization_summary_from_dict = UtilizationSummary.from_dict(utilization_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


