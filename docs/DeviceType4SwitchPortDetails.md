# DeviceType4SwitchPortDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**device** | **str** | Device (either node or IOM) to which the switch port is connected to. | [optional] 
**device_port** | **str** | Port on device that the switch port is connected to | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure** | **str** | Enclosure (cage) to which the switch port is connected to | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. | [optional] 
**ip_address** | **str** | Switch port IP Address | [optional] 
**mac_address** | **str** | MAC address of the switch port | [optional] 
**port_description** | **str** | Switch port description | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**switch_name** | **str** | Switch name. | [optional] 
**switch_port_id** | **int** | ID of the resource | [optional] 
**switch_uid** | **str** | Switch UID | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4_switch_port_details import DeviceType4SwitchPortDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SwitchPortDetails from a JSON string
device_type4_switch_port_details_instance = DeviceType4SwitchPortDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SwitchPortDetails.to_json())

# convert the object into a dict
device_type4_switch_port_details_dict = device_type4_switch_port_details_instance.to_dict()
# create an instance of DeviceType4SwitchPortDetails from a dict
device_type4_switch_port_details_from_dict = DeviceType4SwitchPortDetails.from_dict(device_type4_switch_port_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


