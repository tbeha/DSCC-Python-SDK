# HistogramBucketInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the histogram bucket | [optional] 
**percentage** | **float** | Percentage of I/O in respective histogram bucket | [optional] 
**value** | **float** | Number of I/Os in respective histogram bucket | [optional] 

## Example

```python
from dscc.models.histogram_bucket_inner import HistogramBucketInner

# TODO update the JSON string below
json = "{}"
# create an instance of HistogramBucketInner from a JSON string
histogram_bucket_inner_instance = HistogramBucketInner.from_json(json)
# print the JSON string representation of the object
print(HistogramBucketInner.to_json())

# convert the object into a dict
histogram_bucket_inner_dict = histogram_bucket_inner_instance.to_dict()
# create an instance of HistogramBucketInner from a dict
histogram_bucket_inner_from_dict = HistogramBucketInner.from_dict(histogram_bucket_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


