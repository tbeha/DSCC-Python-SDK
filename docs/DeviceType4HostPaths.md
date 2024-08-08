# DeviceType4HostPaths


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_addr** | **str** | Ip Address | [optional] 
**address** | **str** | WWN Address of the Host Path | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributesDeviceType4HostPath**](CommonResourceAttributesDeviceType4HostPath.md) |  | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain name of the Host | [optional] 
**driver_version** | **str** | Driver version    | [optional] 
**firmware_version** | **str** | Firmware version | [optional] 
**generation** | **int** | Generation Time of the Resource | [optional] 
**host_id** | **int** | ID of the Host resource | [optional] 
**host_name** | **str** | Host Name | [optional] 
**host_speed** | **int** | ID of the Host resource | [optional] 
**id** | **str** | HostPath Resource UID | [optional] 
**model** | **str** | Host Model | [optional] 
**path_type** | **str** | Path Type | [optional] 
**port_pos** | [**DeviceType4HostPathListObjPortPos**](DeviceType4HostPathListObjPortPos.md) |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed hostpath object | [optional] 
**sc_host_initiator_id** | **str** | Host Service Initiator Id | [optional] 
**switch_port_wwn** | **str** | Switch Port WWN | [optional] 
**system_uid** | **str** | System Uid | [optional] 
**system_wwn** | **str** | System serial Number    | [optional] 
**uri** | **str** | Uri  | [optional] 
**vendor** | **str** | Vendor | [optional] 

## Example

```python
from dscc.models.device_type4_host_paths import DeviceType4HostPaths

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostPaths from a JSON string
device_type4_host_paths_instance = DeviceType4HostPaths.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostPaths.to_json())

# convert the object into a dict
device_type4_host_paths_dict = device_type4_host_paths_instance.to_dict()
# create an instance of DeviceType4HostPaths from a dict
device_type4_host_paths_from_dict = DeviceType4HostPaths.from_dict(device_type4_host_paths_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


