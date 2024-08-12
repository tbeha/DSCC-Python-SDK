# QosMetricsData

Timeseries data for particular metric type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | customerId | [optional] 
**items** | [**List[QosMetricSeriesData]**](QosMetricSeriesData.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | total number of series data | [optional] 

## Example

```python
from dscc.models.qos_metrics_data import QosMetricsData

# TODO update the JSON string below
json = "{}"
# create an instance of QosMetricsData from a JSON string
qos_metrics_data_instance = QosMetricsData.from_json(json)
# print the JSON string representation of the object
print(QosMetricsData.to_json())

# convert the object into a dict
qos_metrics_data_dict = qos_metrics_data_instance.to_dict()
# create an instance of QosMetricsData from a dict
qos_metrics_data_from_dict = QosMetricsData.from_dict(qos_metrics_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


