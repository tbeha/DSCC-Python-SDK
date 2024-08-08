# DeviceType4SystemCapacityUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_space** | **float** | Total snap capacity used | [optional] 
**volume_space** | **float** | Total volume capacity used | [optional] 

## Example

```python
from dscc.models.device_type4_system_capacity_usage import DeviceType4SystemCapacityUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SystemCapacityUsage from a JSON string
device_type4_system_capacity_usage_instance = DeviceType4SystemCapacityUsage.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SystemCapacityUsage.to_json())

# convert the object into a dict
device_type4_system_capacity_usage_dict = device_type4_system_capacity_usage_instance.to_dict()
# create an instance of DeviceType4SystemCapacityUsage from a dict
device_type4_system_capacity_usage_from_dict = DeviceType4SystemCapacityUsage.from_dict(device_type4_system_capacity_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


