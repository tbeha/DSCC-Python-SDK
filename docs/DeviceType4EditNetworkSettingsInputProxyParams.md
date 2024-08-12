# DeviceType4EditNetworkSettingsInputProxyParams

Proxy Setting details for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_required** | **str** | Is authentication required. Allowed values are enabled or disabled | [optional] 
**proxy_password** | **str** | Password for authentication. (Required only if Authentication required is enabled). This field is deprecated. | [optional] 
**proxy_port** | **int** | Proxy Server Port. Allowed values are 1-65535 | [optional] 
**proxy_protocol** | **str** | Supported proxy protocols are HTTP, SOCKS4 and SOCKS5. | [optional] 
**proxy_server** | **str** | Proxy server IP address | [optional] 
**proxy_user** | **str** | Username for authentication. (Required only if Authentication required is enabled). This field is deprecated. | [optional] 

## Example

```python
from dscc.models.device_type4_edit_network_settings_input_proxy_params import DeviceType4EditNetworkSettingsInputProxyParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EditNetworkSettingsInputProxyParams from a JSON string
device_type4_edit_network_settings_input_proxy_params_instance = DeviceType4EditNetworkSettingsInputProxyParams.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EditNetworkSettingsInputProxyParams.to_json())

# convert the object into a dict
device_type4_edit_network_settings_input_proxy_params_dict = device_type4_edit_network_settings_input_proxy_params_instance.to_dict()
# create an instance of DeviceType4EditNetworkSettingsInputProxyParams from a dict
device_type4_edit_network_settings_input_proxy_params_from_dict = DeviceType4EditNetworkSettingsInputProxyParams.from_dict(device_type4_edit_network_settings_input_proxy_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


