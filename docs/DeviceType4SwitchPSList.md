# DeviceType4SwitchPSList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**manufacturing** | [**DeviceType4manufacturing**](DeviceType4manufacturing.md) |  | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**resource_uri** | **str** | resourceUri for detailed switch ps object | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**switch_name** | **str** | Switch name | [optional] 
**switch_psid** | **int** | ID of the resource | [optional] 
**switch_uid** | **str** | Switch UID &#x60;Filter&#x60; | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4_switch_ps_list import DeviceType4SwitchPSList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SwitchPSList from a JSON string
device_type4_switch_ps_list_instance = DeviceType4SwitchPSList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SwitchPSList.to_json())

# convert the object into a dict
device_type4_switch_ps_list_dict = device_type4_switch_ps_list_instance.to_dict()
# create an instance of DeviceType4SwitchPSList from a dict
device_type4_switch_ps_list_from_dict = DeviceType4SwitchPSList.from_dict(device_type4_switch_ps_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


