# DeviceType4SwitchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_ip_address** | **str** | Switch active IP Address | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dhcp_servers** | [**List[SwitchDeviceDHCPServerInner]**](SwitchDeviceDHCPServerInner.md) |  | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**fan_state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**fw_version** | **str** | Switch firmware version | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**mac_address** | **str** | MAC address of the switch | [optional] 
**manufacturing** | [**DeviceType4manufacturing**](DeviceType4manufacturing.md) |  | [optional] 
**mode** | **str** | Switch mode | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter&#x60; | [optional] 
**primary_path** | **str** | Switch primary path state | [optional] 
**ps1_state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**ps2_state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed switch object | [optional] 
**secondary_path** | **str** | Switch secondary path state | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**switch_id** | **int** | ID of the resource | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**temperature_detail** | **str** | Switch mode | [optional] 
**temperature_state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**type** | **str** | type | [optional] 
**vlans** | [**List[SwitchDeviceVlanInner]**](SwitchDeviceVlanInner.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_switch_list import DeviceType4SwitchList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SwitchList from a JSON string
device_type4_switch_list_instance = DeviceType4SwitchList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SwitchList.to_json())

# convert the object into a dict
device_type4_switch_list_dict = device_type4_switch_list_instance.to_dict()
# create an instance of DeviceType4SwitchList from a dict
device_type4_switch_list_from_dict = DeviceType4SwitchList.from_dict(device_type4_switch_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


