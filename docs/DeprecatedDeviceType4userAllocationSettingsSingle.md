# DeprecatedDeviceType4userAllocationSettingsSingle

This field is deprecated.

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
from dscc.models.deprecated_device_type4user_allocation_settings_single import DeprecatedDeviceType4userAllocationSettingsSingle

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatedDeviceType4userAllocationSettingsSingle from a JSON string
deprecated_device_type4user_allocation_settings_single_instance = DeprecatedDeviceType4userAllocationSettingsSingle.from_json(json)
# print the JSON string representation of the object
print(DeprecatedDeviceType4userAllocationSettingsSingle.to_json())

# convert the object into a dict
deprecated_device_type4user_allocation_settings_single_dict = deprecated_device_type4user_allocation_settings_single_instance.to_dict()
# create an instance of DeprecatedDeviceType4userAllocationSettingsSingle from a dict
deprecated_device_type4user_allocation_settings_single_from_dict = DeprecatedDeviceType4userAllocationSettingsSingle.from_dict(deprecated_device_type4user_allocation_settings_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


