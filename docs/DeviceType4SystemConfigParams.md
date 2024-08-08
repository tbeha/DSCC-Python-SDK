# DeviceType4SystemConfigParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**DeviceType4systemSettingsDetails**](DeviceType4systemSettingsDetails.md) |  | [optional] 
**request_uri** | **str** | requestUri for system settings details | [optional] 

## Example

```python
from dscc.models.device_type4_system_config_params import DeviceType4SystemConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SystemConfigParams from a JSON string
device_type4_system_config_params_instance = DeviceType4SystemConfigParams.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SystemConfigParams.to_json())

# convert the object into a dict
device_type4_system_config_params_dict = device_type4_system_config_params_instance.to_dict()
# create an instance of DeviceType4SystemConfigParams from a dict
device_type4_system_config_params_from_dict = DeviceType4SystemConfigParams.from_dict(device_type4_system_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


