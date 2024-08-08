# DeviceType4userAllocationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ha** | [**DeprecatedDeviceType4userAllocationSettingsSingleHA**](DeprecatedDeviceType4userAllocationSettingsSingleHA.md) |  | [optional] 
**raid_type** | **str** |  | [optional] 
**device_speed** | [**DeviceType4deviceSpeed**](DeviceType4deviceSpeed.md) |  | [optional] 
**device_type** | **str** |  | [optional] 
**disk_filter** | **str** |  | [optional] 
**requested_ha** | [**DeprecatedDeviceType4userAllocationSettingsSingleHA**](DeprecatedDeviceType4userAllocationSettingsSingleHA.md) |  | [optional] 
**set_size** | **str** |  | [optional] 
**step_size** | **int** |  | [optional] 

## Example

```python
from dscc.models.device_type4user_allocation_settings import DeviceType4userAllocationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4userAllocationSettings from a JSON string
device_type4user_allocation_settings_instance = DeviceType4userAllocationSettings.from_json(json)
# print the JSON string representation of the object
print(DeviceType4userAllocationSettings.to_json())

# convert the object into a dict
device_type4user_allocation_settings_dict = device_type4user_allocation_settings_instance.to_dict()
# create an instance of DeviceType4userAllocationSettings from a dict
device_type4user_allocation_settings_from_dict = DeviceType4userAllocationSettings.from_dict(device_type4user_allocation_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


