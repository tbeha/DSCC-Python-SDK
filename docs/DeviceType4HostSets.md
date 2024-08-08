# DeviceType4HostSets

Host Sets details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**comment** | **str** | Comment on the Host Set | [optional] 
**common_resource_attributes** | [**CommonResourceAttributesDeviceType4HostSet**](CommonResourceAttributesDeviceType4HostSet.md) |  | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain name of the Host Set | [optional] 
**generation** | **int** | Generation Time of the Resource | [optional] 
**host_set_id** | **int** | Numeric ID of the resource | [optional] 
**id** | **str** | HostSet Resource UID | [optional] 
**members** | **List[Optional[str]]** | system ntp addresses | [optional] 
**name** | **str** | Host Set Name | [optional] 
**resource_uri** | **str** | resourceUri for detailed hostset object | [optional] 
**sc_host_group_id** | **str** | Host Service HostGroup Id | [optional] 
**system_uid** | **str** | Serail Number of the system | [optional] 
**system_wwn** | **str** | System wwn | [optional] 
**uri** | **str** | Uri | [optional] 
**uuid** | **str** | HostSet Resource UUID | [optional] 

## Example

```python
from dscc.models.device_type4_host_sets import DeviceType4HostSets

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostSets from a JSON string
device_type4_host_sets_instance = DeviceType4HostSets.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostSets.to_json())

# convert the object into a dict
device_type4_host_sets_dict = device_type4_host_sets_instance.to_dict()
# create an instance of DeviceType4HostSets from a dict
device_type4_host_sets_from_dict = DeviceType4HostSets.from_dict(device_type4_host_sets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


