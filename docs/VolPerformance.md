# VolPerformance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**iops** | [**NimbleKpiMetrics**](NimbleKpiMetrics.md) |  | [optional] 
**latency** | [**NimbleKpiMetrics**](NimbleKpiMetrics.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed volume object | [optional] 
**resource_uri** | **str** | resourceUri for detailed volume object | [optional] 
**throughput** | [**NimbleKpiMetrics**](NimbleKpiMetrics.md) |  | [optional] 

## Example

```python
from dscc.models.vol_performance import VolPerformance

# TODO update the JSON string below
json = "{}"
# create an instance of VolPerformance from a JSON string
vol_performance_instance = VolPerformance.from_json(json)
# print the JSON string representation of the object
print(VolPerformance.to_json())

# convert the object into a dict
vol_performance_dict = vol_performance_instance.to_dict()
# create an instance of VolPerformance from a dict
vol_performance_from_dict = VolPerformance.from_dict(vol_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


