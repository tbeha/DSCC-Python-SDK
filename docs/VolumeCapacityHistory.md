# VolumeCapacityHistory

volume capacity trends for given granularity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_data** | [**VolumeCapacityHistoryCapacityData**](VolumeCapacityHistoryCapacityData.md) |  | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**end_time** | **int** | end time of the capacity history | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**start_time** | **int** | start time of the capacity history | [optional] 

## Example

```python
from dscc.models.volume_capacity_history import VolumeCapacityHistory

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeCapacityHistory from a JSON string
volume_capacity_history_instance = VolumeCapacityHistory.from_json(json)
# print the JSON string representation of the object
print(VolumeCapacityHistory.to_json())

# convert the object into a dict
volume_capacity_history_dict = volume_capacity_history_instance.to_dict()
# create an instance of VolumeCapacityHistory from a dict
volume_capacity_history_from_dict = VolumeCapacityHistory.from_dict(volume_capacity_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


