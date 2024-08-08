# NimbleKpiMetrics

kpi metrics with read, write and total average values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | [**NimbleperfData**](NimbleperfData.md) |  | [optional] 
**total** | [**NimbleperfData**](NimbleperfData.md) |  | [optional] 
**write** | [**NimbleperfData**](NimbleperfData.md) |  | [optional] 

## Example

```python
from dscc.models.nimble_kpi_metrics import NimbleKpiMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleKpiMetrics from a JSON string
nimble_kpi_metrics_instance = NimbleKpiMetrics.from_json(json)
# print the JSON string representation of the object
print(NimbleKpiMetrics.to_json())

# convert the object into a dict
nimble_kpi_metrics_dict = nimble_kpi_metrics_instance.to_dict()
# create an instance of NimbleKpiMetrics from a dict
nimble_kpi_metrics_from_dict = NimbleKpiMetrics.from_dict(nimble_kpi_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


