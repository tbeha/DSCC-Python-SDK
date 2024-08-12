# DeviceType4SwitchFanDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. | [optional] 
**manufacturing** | [**DeviceType4manufacturing**](DeviceType4manufacturing.md) |  | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**speed_a** | **str** | Switch fan speed | [optional] 
**speed_b** | **str** | Switch fan speed | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**state_a** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**state_b** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**switch_fan_id** | **int** | ID of the resource | [optional] 
**switch_name** | **str** | Switch name | [optional] 
**switch_uid** | **str** | Switch UID | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4_switch_fan_details import DeviceType4SwitchFanDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SwitchFanDetails from a JSON string
device_type4_switch_fan_details_instance = DeviceType4SwitchFanDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SwitchFanDetails.to_json())

# convert the object into a dict
device_type4_switch_fan_details_dict = device_type4_switch_fan_details_instance.to_dict()
# create an instance of DeviceType4SwitchFanDetails from a dict
device_type4_switch_fan_details_from_dict = DeviceType4SwitchFanDetails.from_dict(device_type4_switch_fan_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


