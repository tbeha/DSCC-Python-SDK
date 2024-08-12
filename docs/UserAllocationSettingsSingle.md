# UserAllocationSettingsSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ha** | [**DeprecatedDeviceType4userAllocationSettingsSingleHA**](DeprecatedDeviceType4userAllocationSettingsSingleHA.md) |  | [optional] 
**raid_type** | **str** |  | [optional] 
**device_speed** | [**DeviceSpeedSingle**](DeviceSpeedSingle.md) |  | [optional] 
**device_type** | **str** |  | [optional] 
**disk_filter** | **str** |  | [optional] 
**requested_ha** | [**DeprecatedDeviceType4userAllocationSettingsSingleHA**](DeprecatedDeviceType4userAllocationSettingsSingleHA.md) |  | [optional] 
**set_size** | **str** |  | [optional] 
**step_size** | **int** |  | [optional] 

## Example

```python
from dscc.models.user_allocation_settings_single import UserAllocationSettingsSingle

# TODO update the JSON string below
json = "{}"
# create an instance of UserAllocationSettingsSingle from a JSON string
user_allocation_settings_single_instance = UserAllocationSettingsSingle.from_json(json)
# print the JSON string representation of the object
print(UserAllocationSettingsSingle.to_json())

# convert the object into a dict
user_allocation_settings_single_dict = user_allocation_settings_single_instance.to_dict()
# create an instance of UserAllocationSettingsSingle from a dict
user_allocation_settings_single_from_dict = UserAllocationSettingsSingle.from_dict(user_allocation_settings_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


