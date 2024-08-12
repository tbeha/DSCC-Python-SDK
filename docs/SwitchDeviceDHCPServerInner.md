# SwitchDeviceDHCPServerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | DHCP status | [optional] 
**vrf_name** | **str** | DHCP VRF Name | [optional] 

## Example

```python
from dscc.models.switch_device_dhcp_server_inner import SwitchDeviceDHCPServerInner

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchDeviceDHCPServerInner from a JSON string
switch_device_dhcp_server_inner_instance = SwitchDeviceDHCPServerInner.from_json(json)
# print the JSON string representation of the object
print(SwitchDeviceDHCPServerInner.to_json())

# convert the object into a dict
switch_device_dhcp_server_inner_dict = switch_device_dhcp_server_inner_instance.to_dict()
# create an instance of SwitchDeviceDHCPServerInner from a dict
switch_device_dhcp_server_inner_from_dict = SwitchDeviceDHCPServerInner.from_dict(switch_device_dhcp_server_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


