# DeviceType4SwitchPortList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**device** | **str** | Device (either node or IOM) to which the switch port is connected to | [optional] 
**device_port** | **str** | Port on device that the switch port is connected to | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure** | **str** | Enclosure (cage) to which the switch port is connected to | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**ip_address** | **str** | Switch port IP Address | [optional] 
**mac_address** | **str** | MAC address of the switch port | [optional] 
**port_description** | **str** | Switch port description | [optional] 
**resource_uri** | **str** | resourceUri for detailed switch port object | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**switch_name** | **str** | Switch name. | [optional] 
**switch_port_id** | **int** | ID of the resource | [optional] 
**switch_uid** | **str** | Switch UID | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4_switch_port_list import DeviceType4SwitchPortList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SwitchPortList from a JSON string
device_type4_switch_port_list_instance = DeviceType4SwitchPortList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SwitchPortList.to_json())

# convert the object into a dict
device_type4_switch_port_list_dict = device_type4_switch_port_list_instance.to_dict()
# create an instance of DeviceType4SwitchPortList from a dict
device_type4_switch_port_list_from_dict = DeviceType4SwitchPortList.from_dict(device_type4_switch_port_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


