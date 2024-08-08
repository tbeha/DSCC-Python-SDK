# VolumeCapacityHistoryCapacityData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | customerId | [optional] 
**items** | [**List[VolumeCapacitySeriesData]**](VolumeCapacitySeriesData.md) |  | [optional] 
**total** | **int** | count of series data | [optional] 

## Example

```python
from dscc.models.volume_capacity_history_capacity_data import VolumeCapacityHistoryCapacityData

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeCapacityHistoryCapacityData from a JSON string
volume_capacity_history_capacity_data_instance = VolumeCapacityHistoryCapacityData.from_json(json)
# print the JSON string representation of the object
print(VolumeCapacityHistoryCapacityData.to_json())

# convert the object into a dict
volume_capacity_history_capacity_data_dict = volume_capacity_history_capacity_data_instance.to_dict()
# create an instance of VolumeCapacityHistoryCapacityData from a dict
volume_capacity_history_capacity_data_from_dict = VolumeCapacityHistoryCapacityData.from_dict(volume_capacity_history_capacity_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


