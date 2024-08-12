# QosPerformanceHistory

qos performance trends for given granularity and time range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**qos_metrics_data** | [**QosMetricsData**](QosMetricsData.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 

## Example

```python
from dscc.models.qos_performance_history import QosPerformanceHistory

# TODO update the JSON string below
json = "{}"
# create an instance of QosPerformanceHistory from a JSON string
qos_performance_history_instance = QosPerformanceHistory.from_json(json)
# print the JSON string representation of the object
print(QosPerformanceHistory.to_json())

# convert the object into a dict
qos_performance_history_dict = qos_performance_history_instance.to_dict()
# create an instance of QosPerformanceHistory from a dict
qos_performance_history_from_dict = QosPerformanceHistory.from_dict(qos_performance_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


