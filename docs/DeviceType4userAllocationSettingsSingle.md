# DeviceType4userAllocationSettingsSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ha** | [**DeprecatedDeviceType4userAllocationSettingsSingleHA**](DeprecatedDeviceType4userAllocationSettingsSingleHA.md) |  | [optional] 
**raid_type** | **str** |  | [optional] 
**device_speed** | [**DeviceType4deviceSpeedSingle**](DeviceType4deviceSpeedSingle.md) |  | [optional] 
**device_type** | **str** |  | [optional] 
**disk_filter** | **str** |  | [optional] 
**requested_ha** | [**DeprecatedDeviceType4userAllocationSettingsSingleHA**](DeprecatedDeviceType4userAllocationSettingsSingleHA.md) |  | [optional] 
**set_size** | **str** |  | [optional] 
**step_size** | **int** |  | [optional] 

## Example

```python
from dscc.models.device_type4user_allocation_settings_single import DeviceType4userAllocationSettingsSingle

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4userAllocationSettingsSingle from a JSON string
device_type4user_allocation_settings_single_instance = DeviceType4userAllocationSettingsSingle.from_json(json)
# print the JSON string representation of the object
print(DeviceType4userAllocationSettingsSingle.to_json())

# convert the object into a dict
device_type4user_allocation_settings_single_dict = device_type4user_allocation_settings_single_instance.to_dict()
# create an instance of DeviceType4userAllocationSettingsSingle from a dict
device_type4user_allocation_settings_single_from_dict = DeviceType4userAllocationSettingsSingle.from_dict(device_type4user_allocation_settings_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


