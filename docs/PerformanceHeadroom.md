# PerformanceHeadroom

System performance Headroom

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_headroom** | **str** | Available Headroom on the systems (High Medium or Low) | [optional] 
**headroom_utilization** | **str** | Headroom Utilization on the systems (High Medium or Low) | [optional] 
**utilization** | **float** | Utilization in percentage | [optional] 

## Example

```python
from dscc.models.performance_headroom import PerformanceHeadroom

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceHeadroom from a JSON string
performance_headroom_instance = PerformanceHeadroom.from_json(json)
# print the JSON string representation of the object
print(PerformanceHeadroom.to_json())

# convert the object into a dict
performance_headroom_dict = performance_headroom_instance.to_dict()
# create an instance of PerformanceHeadroom from a dict
performance_headroom_from_dict = PerformanceHeadroom.from_dict(performance_headroom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


