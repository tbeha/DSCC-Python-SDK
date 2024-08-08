# DeviceType4VolumePerformanceHistogram

Response structure of performance histogram

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Id specific to the customer | [optional] 
**end_time** | **float** | End time for volume histogram data | [optional] 
**request_uri** | **str** | requestUri for performance histogram | [optional] 
**size_histogram_data** | [**SizeHistogramData**](SizeHistogramData.md) |  | [optional] 
**start_time** | **float** | Start time for volume histogram data | [optional] 

## Example

```python
from dscc.models.device_type4_volume_performance_histogram import DeviceType4VolumePerformanceHistogram

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VolumePerformanceHistogram from a JSON string
device_type4_volume_performance_histogram_instance = DeviceType4VolumePerformanceHistogram.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VolumePerformanceHistogram.to_json())

# convert the object into a dict
device_type4_volume_performance_histogram_dict = device_type4_volume_performance_histogram_instance.to_dict()
# create an instance of DeviceType4VolumePerformanceHistogram from a dict
device_type4_volume_performance_histogram_from_dict = DeviceType4VolumePerformanceHistogram.from_dict(device_type4_volume_performance_histogram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


