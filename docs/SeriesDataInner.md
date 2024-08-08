# SeriesDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_buckets** | [**List[HistogramBucketInner]**](HistogramBucketInner.md) | Histogram data of io buckets | [optional] 
**timestamp** | **float** | Timestamp in epoch milliseconds for which the metrics are listed | [optional] 
**write_buckets** | [**List[HistogramBucketInner]**](HistogramBucketInner.md) | Histogram data of io buckets | [optional] 

## Example

```python
from dscc.models.series_data_inner import SeriesDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesDataInner from a JSON string
series_data_inner_instance = SeriesDataInner.from_json(json)
# print the JSON string representation of the object
print(SeriesDataInner.to_json())

# convert the object into a dict
series_data_inner_dict = series_data_inner_instance.to_dict()
# create an instance of SeriesDataInner from a dict
series_data_inner_from_dict = SeriesDataInner.from_dict(series_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


