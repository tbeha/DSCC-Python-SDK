# LatencyAnnotationMetrics

Volume latency annotations response structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latency_qtl90** | **float** | Value of 90th quantile of time histogram | [optional] 
**max_range** | **str** | Maximum range of values in time histogram | [optional] 
**timestamp_ms** | **float** | Timestamp in milliseconds | [optional] 

## Example

```python
from dscc.models.latency_annotation_metrics import LatencyAnnotationMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of LatencyAnnotationMetrics from a JSON string
latency_annotation_metrics_instance = LatencyAnnotationMetrics.from_json(json)
# print the JSON string representation of the object
print(LatencyAnnotationMetrics.to_json())

# convert the object into a dict
latency_annotation_metrics_dict = latency_annotation_metrics_instance.to_dict()
# create an instance of LatencyAnnotationMetrics from a dict
latency_annotation_metrics_from_dict = LatencyAnnotationMetrics.from_dict(latency_annotation_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


