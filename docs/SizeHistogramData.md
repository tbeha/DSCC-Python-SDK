# SizeHistogramData

Size histogram data structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggs** | [**Aggregations**](Aggregations.md) |  | [optional] 
**series_data** | [**List[SeriesDataInner]**](SeriesDataInner.md) | Size histogram data structure | [optional] 

## Example

```python
from dscc.models.size_histogram_data import SizeHistogramData

# TODO update the JSON string below
json = "{}"
# create an instance of SizeHistogramData from a JSON string
size_histogram_data_instance = SizeHistogramData.from_json(json)
# print the JSON string representation of the object
print(SizeHistogramData.to_json())

# convert the object into a dict
size_histogram_data_dict = size_histogram_data_instance.to_dict()
# create an instance of SizeHistogramData from a dict
size_histogram_data_from_dict = SizeHistogramData.from_dict(size_histogram_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


