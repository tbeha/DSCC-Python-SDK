# DeviceType4SupportSettingsInput

Edit Support settings for the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connect_to_hpe** | **str** | Enable remote support by allowing sending of files from device to HPE. Allowed values: enabled or disabled. It is mandatory. | 
**device_id** | **str** | Id of the array. User can get Id info from GET response. It is mandatory. | [optional] 
**enterprise_server_url** | **str** | Callhome collection server URL | [optional] 
**mini_insplore_enabled** | **str** | Enables/Disable scheduled Mini-Insplore collection. Allowed values: enabled or disabled. | [optional] 
**remote_access** | **str** | Allow HPE Support to access the device remotely. Allowed values: ENABLE_ROOT or DISABLE or ENABLE_NONROOT. It is mandatory. | 

## Example

```python
from dscc.models.device_type4_support_settings_input import DeviceType4SupportSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SupportSettingsInput from a JSON string
device_type4_support_settings_input_instance = DeviceType4SupportSettingsInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SupportSettingsInput.to_json())

# convert the object into a dict
device_type4_support_settings_input_dict = device_type4_support_settings_input_instance.to_dict()
# create an instance of DeviceType4SupportSettingsInput from a dict
device_type4_support_settings_input_from_dict = DeviceType4SupportSettingsInput.from_dict(device_type4_support_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


