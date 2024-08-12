# DeviceType4networkSettings

Network-Settings details for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_management** | [**DeviceType4sysPortManagement**](DeviceType4sysPortManagement.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object  | [optional] 

## Example

```python
from dscc.models.device_type4network_settings import DeviceType4networkSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4networkSettings from a JSON string
device_type4network_settings_instance = DeviceType4networkSettings.from_json(json)
# print the JSON string representation of the object
print(DeviceType4networkSettings.to_json())

# convert the object into a dict
device_type4network_settings_dict = device_type4network_settings_instance.to_dict()
# create an instance of DeviceType4networkSettings from a dict
device_type4network_settings_from_dict = DeviceType4networkSettings.from_dict(device_type4network_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


