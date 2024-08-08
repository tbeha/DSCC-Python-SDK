# KpiMetrics

kpi metrics with read, write and total average values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | [**PmPerfData**](PmPerfData.md) |  | [optional] 
**total** | [**PmPerfData**](PmPerfData.md) |  | [optional] 
**write** | [**PmPerfData**](PmPerfData.md) |  | [optional] 

## Example

```python
from dscc.models.kpi_metrics import KpiMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of KpiMetrics from a JSON string
kpi_metrics_instance = KpiMetrics.from_json(json)
# print the JSON string representation of the object
print(KpiMetrics.to_json())

# convert the object into a dict
kpi_metrics_dict = kpi_metrics_instance.to_dict()
# create an instance of KpiMetrics from a dict
kpi_metrics_from_dict = KpiMetrics.from_dict(kpi_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


