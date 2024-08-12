# EditNetworkSettingsInput

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
**proxy_params** | [**EditNetworkSettingsInputProxyParams**](EditNetworkSettingsInputProxyParams.md) |  | [optional] 

## Example

```python
from dscc.models.edit_network_settings_input import EditNetworkSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of EditNetworkSettingsInput from a JSON string
edit_network_settings_input_instance = EditNetworkSettingsInput.from_json(json)
# print the JSON string representation of the object
print(EditNetworkSettingsInput.to_json())

# convert the object into a dict
edit_network_settings_input_dict = edit_network_settings_input_instance.to_dict()
# create an instance of EditNetworkSettingsInput from a dict
edit_network_settings_input_from_dict = EditNetworkSettingsInput.from_dict(edit_network_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


