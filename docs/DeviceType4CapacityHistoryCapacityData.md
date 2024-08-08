# DeviceType4CapacityHistoryCapacityData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | customerId | [optional] 
**items** | [**List[DeviceType4capacitySeriesData]**](DeviceType4capacitySeriesData.md) |  | [optional] 
**total** | **int** | count of series data | [optional] 

## Example

```python
from dscc.models.device_type4_capacity_history_capacity_data import DeviceType4CapacityHistoryCapacityData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CapacityHistoryCapacityData from a JSON string
device_type4_capacity_history_capacity_data_instance = DeviceType4CapacityHistoryCapacityData.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CapacityHistoryCapacityData.to_json())

# convert the object into a dict
device_type4_capacity_history_capacity_data_dict = device_type4_capacity_history_capacity_data_instance.to_dict()
# create an instance of DeviceType4CapacityHistoryCapacityData from a dict
device_type4_capacity_history_capacity_data_from_dict = DeviceType4CapacityHistoryCapacityData.from_dict(device_type4_capacity_history_capacity_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


