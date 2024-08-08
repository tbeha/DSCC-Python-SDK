# DeviceType4CapacityHistory

capacity performance trends for given granularity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_data** | [**DeviceType4CapacityHistoryCapacityData**](DeviceType4CapacityHistoryCapacityData.md) |  | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**end_time** | **int** | end time of the capacity history | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**start_time** | **int** | start time of the capacity history | [optional] 

## Example

```python
from dscc.models.device_type4_capacity_history import DeviceType4CapacityHistory

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CapacityHistory from a JSON string
device_type4_capacity_history_instance = DeviceType4CapacityHistory.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CapacityHistory.to_json())

# convert the object into a dict
device_type4_capacity_history_dict = device_type4_capacity_history_instance.to_dict()
# create an instance of DeviceType4CapacityHistory from a dict
device_type4_capacity_history_from_dict = DeviceType4CapacityHistory.from_dict(device_type4_capacity_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


