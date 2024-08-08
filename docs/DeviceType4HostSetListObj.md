# DeviceType4HostSetListObj

Host Sets details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**comment** | **str** | Comment on the Host Set | [optional] 
**common_resource_attributes** | [**CommonResourceAttributesDeviceType4HostSet**](CommonResourceAttributesDeviceType4HostSet.md) |  | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain name of the Host Set | [optional] 
**generation** | **int** | Generation Time of the Resource &#x60;Filter, Sort&#x60; | [optional] 
**host_set_id** | **int** | Numeric ID of the resource | [optional] 
**id** | **str** | HostSet Resource UID &#x60;Filter&#x60; | [optional] 
**members** | **List[Optional[str]]** | system ntp addresses &#x60;Filter, Sort&#x60; | [optional] 
**name** | **str** | Host Set Name &#x60;Filter, Sort&#x60; | [optional] 
**resource_uri** | **str** | resourceUri for detailed hostset object | [optional] 
**sc_host_group_id** | **str** | Host Service HostGroup Id &#x60;Filter&#x60; | [optional] 
**system_uid** | **str** | Serail Number of the system &#x60;Filter&#x60; | [optional] 
**system_wwn** | **str** | System wwn &#x60;Filter, Sort&#x60; | [optional] 
**uri** | **str** | Uri | [optional] 
**uuid** | **str** | HostSet Resource UUID | [optional] 

## Example

```python
from dscc.models.device_type4_host_set_list_obj import DeviceType4HostSetListObj

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostSetListObj from a JSON string
device_type4_host_set_list_obj_instance = DeviceType4HostSetListObj.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostSetListObj.to_json())

# convert the object into a dict
device_type4_host_set_list_obj_dict = device_type4_host_set_list_obj_instance.to_dict()
# create an instance of DeviceType4HostSetListObj from a dict
device_type4_host_set_list_obj_from_dict = DeviceType4HostSetListObj.from_dict(device_type4_host_set_list_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


