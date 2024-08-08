# DriftsDetectedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_end_time** | **float** | Actual end time of the Drift. | [optional] 
**actual_start_time** | **float** | Actual start time of the Drift. | [optional] 
**avg90th_percentile** | **float** | 90th quantile of latency | [optional] 
**drift_buckets** | [**List[DriftBucketsInner]**](DriftBucketsInner.md) | IO size buckets in which drifts are observed | [optional] 
**end_time** | **float** | End time of the Drift | [optional] 
**io_type** | **str** | Drift detected in operation type | [optional] 
**latency_range_unit** | **str** | Metric of the latency range | [optional] 
**max_latency_lower_range** | **float** | Floor of the latency bucket | [optional] 
**max_latency_upper_range** | **float** | Ceiling of the latency bucket | [optional] 
**start_time** | **float** | Start time of the Drift | [optional] 
**updated** | **bool** | Specifies if the values are changed. | [optional] 

## Example

```python
from dscc.models.drifts_detected_inner import DriftsDetectedInner

# TODO update the JSON string below
json = "{}"
# create an instance of DriftsDetectedInner from a JSON string
drifts_detected_inner_instance = DriftsDetectedInner.from_json(json)
# print the JSON string representation of the object
print(DriftsDetectedInner.to_json())

# convert the object into a dict
drifts_detected_inner_dict = drifts_detected_inner_instance.to_dict()
# create an instance of DriftsDetectedInner from a dict
drifts_detected_inner_from_dict = DriftsDetectedInner.from_dict(drifts_detected_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


