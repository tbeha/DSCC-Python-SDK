# DeviceType4HostPathListObj


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_addr** | **str** | Ip Address | [optional] 
**address** | **str** | WWN Address of the Host Path &#x60;Filter&#x60; | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributesDeviceType4HostPath**](CommonResourceAttributesDeviceType4HostPath.md) |  | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain name of the Host | [optional] 
**driver_version** | **str** | Driver version    | [optional] 
**firmware_version** | **str** | Firmware version | [optional] 
**generation** | **int** | Generation Time of the Resource &#x60;Filter, Sort&#x60; | [optional] 
**host_id** | **int** | ID of the Host resource | [optional] 
**host_name** | **str** | Host Name &#x60;Filter, Sort&#x60; | [optional] 
**host_speed** | **int** | ID of the Host resource | [optional] 
**id** | **str** | HostPath Resource UID &#x60;Filter&#x60; | [optional] 
**model** | **str** | Host Model | [optional] 
**path_type** | **str** | Path Type &#x60;Filter&#x60; | [optional] 
**port_pos** | [**DeviceType4HostPathListObjPortPos**](DeviceType4HostPathListObjPortPos.md) |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed hostpath object | [optional] 
**sc_host_initiator_id** | **str** | Host Service Initiator Id &#x60;Filter&#x60; | [optional] 
**switch_port_wwn** | **str** | Switch Port WWN | [optional] 
**system_uid** | **str** | System Uid &#x60;Filter&#x60; | [optional] 
**system_wwn** | **str** | System serial Number &#x60;Filter, Sort&#x60; | [optional] 
**uri** | **str** | Uri  | [optional] 
**vendor** | **str** | Vendor | [optional] 

## Example

```python
from dscc.models.device_type4_host_path_list_obj import DeviceType4HostPathListObj

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostPathListObj from a JSON string
device_type4_host_path_list_obj_instance = DeviceType4HostPathListObj.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostPathListObj.to_json())

# convert the object into a dict
device_type4_host_path_list_obj_dict = device_type4_host_path_list_obj_instance.to_dict()
# create an instance of DeviceType4HostPathListObj from a dict
device_type4_host_path_list_obj_from_dict = DeviceType4HostPathListObj.from_dict(device_type4_host_path_list_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


