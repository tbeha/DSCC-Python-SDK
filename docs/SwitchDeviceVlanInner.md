# SwitchDeviceVlanInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operational_state** | **str** | Status of vlan | [optional] 
**vlan_id** | **int** | Vlan ID | [optional] 
**vlan_name** | **str** | Vlan Name | [optional] 

## Example

```python
from dscc.models.switch_device_vlan_inner import SwitchDeviceVlanInner

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchDeviceVlanInner from a JSON string
switch_device_vlan_inner_instance = SwitchDeviceVlanInner.from_json(json)
# print the JSON string representation of the object
print(SwitchDeviceVlanInner.to_json())

# convert the object into a dict
switch_device_vlan_inner_dict = switch_device_vlan_inner_instance.to_dict()
# create an instance of SwitchDeviceVlanInner from a dict
switch_device_vlan_inner_from_dict = SwitchDeviceVlanInner.from_dict(switch_device_vlan_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


