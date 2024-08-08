# QosMetricSeriesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bw_limit_kbps** | **float** | throughput threshold at particular timestamp | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**generation** | **int** | generation | [optional] 
**timestampms** | **int** | epoch timestamp | [optional] 
**type** | **str** | type | [optional] 
**wqlen** | **float** | wait qlen value at particular timestamp | [optional] 

## Example

```python
from dscc.models.qos_metric_series_data import QosMetricSeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of QosMetricSeriesData from a JSON string
qos_metric_series_data_instance = QosMetricSeriesData.from_json(json)
# print the JSON string representation of the object
print(QosMetricSeriesData.to_json())

# convert the object into a dict
qos_metric_series_data_dict = qos_metric_series_data_instance.to_dict()
# create an instance of QosMetricSeriesData from a dict
qos_metric_series_data_from_dict = QosMetricSeriesData.from_dict(qos_metric_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


