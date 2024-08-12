# DeviceType4EditNetworkSettingsInput

Proxy Setting details for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_addresses** | **List[str]** | Dns address of the system | [optional] 
**ipv4_address** | **str** | ipv4 address of the system | [optional] 
**ipv4_gateway** | **str** | ipv4 gateway of the system | [optional] 
**ipv4_subnet_mask** | **str** | NetMask for IPV4 address | [optional] 
**ipv6_address** | **str** | IPV6 address of the system | [optional] 
**ipv6_gateway** | **str** | IPV6 address of the system | [optional] 
**ipv6_prefix_len** | **str** | IPV6 Prefix length | [optional] 
**proxy_params** | [**DeviceType4EditNetworkSettingsInputProxyParams**](DeviceType4EditNetworkSettingsInputProxyParams.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_edit_network_settings_input import DeviceType4EditNetworkSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EditNetworkSettingsInput from a JSON string
device_type4_edit_network_settings_input_instance = DeviceType4EditNetworkSettingsInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EditNetworkSettingsInput.to_json())

# convert the object into a dict
device_type4_edit_network_settings_input_dict = device_type4_edit_network_settings_input_instance.to_dict()
# create an instance of DeviceType4EditNetworkSettingsInput from a dict
device_type4_edit_network_settings_input_from_dict = DeviceType4EditNetworkSettingsInput.from_dict(device_type4_edit_network_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


