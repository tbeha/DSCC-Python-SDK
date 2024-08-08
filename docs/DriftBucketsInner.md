# DriftBucketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **float** | Bucket name in which drifts are detected | [optional] 
**bucket_unit** | **str** | Metric of the bucket in which drift is detected | [optional] 
**magnitude** | **float** | Quantity of workload change in the bucket where drift detected | [optional] 

## Example

```python
from dscc.models.drift_buckets_inner import DriftBucketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DriftBucketsInner from a JSON string
drift_buckets_inner_instance = DriftBucketsInner.from_json(json)
# print the JSON string representation of the object
print(DriftBucketsInner.to_json())

# convert the object into a dict
drift_buckets_inner_dict = drift_buckets_inner_instance.to_dict()
# create an instance of DriftBucketsInner from a dict
drift_buckets_inner_from_dict = DriftBucketsInner.from_dict(drift_buckets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


