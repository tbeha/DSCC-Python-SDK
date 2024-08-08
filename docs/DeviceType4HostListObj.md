# DeviceType4HostListObj

HPE Alletra Storage MP Host details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | [**DeviceType4HostAgent**](DeviceType4HostAgent.md) |  | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributesDeviceType4Host**](CommonResourceAttributesDeviceType4Host.md) |  | [optional] 
**descriptors** | [**DeviceType4HostDescriptors**](DeviceType4HostDescriptors.md) |  | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain name of the Host | [optional] 
**generation** | **int** | Generation Time of the Resource &#x60;Filter, Sort&#x60; | [optional] 
**host_id** | **int** | Numeric ID of the resource | [optional] 
**hostpaths** | [**List[DeviceType4HostPathDetailsForDeviceType4Host]**](DeviceType4HostPathDetailsForDeviceType4Host.md) |  | [optional] 
**id** | **str** | Host Resource UID &#x60;Filter&#x60; | [optional] 
**initiator_chap_enabled** | **bool** | Indicates if the Initiator Chap is enabled or not | [optional] 
**initiator_chap_name** | **str** | Initiator Chap Name | [optional] 
**initiator_encrypted_chap_secret** | **str** | Initiator Encrypted Chap Secret | [optional] 
**is_vvol_host** | **bool** | Indicates if this host is used to export VASA vVol over NVMe Protocol. | [optional] 
**min_lun_id** | **int** | LUN Id of the host | [optional] 
**name** | **str** | Host Name &#x60;Filter, Sort&#x60; | [optional] 
**persona** | [**DeviceType4Persona**](DeviceType4Persona.md) |  | [optional] 
**resource_uri** | **str** | Resoure Uri of the Host         | [optional] 
**sc_host_id** | **str** | Host Service Host Id &#x60;Filter&#x60; | [optional] 
**state** | [**DeviceType4HostState**](DeviceType4HostState.md) |  | [optional] 
**state_description** | **List[Optional[str]]** |  | [optional] 
**state_val** | **int** | Health Status of the Host | [optional] 
**system_uid** | **str** | Serial Number of the system &#x60;Filter&#x60;   | [optional] 
**system_wwn** | **str** | System wwn &#x60;Filter, Sort&#x60; | [optional] 
**target_chap_enabled** | **bool** | Indicates if the Target Chap is enabled or not | [optional] 
**target_chap_name** | **str** | Target Chap Name | [optional] 
**target_encrypted_chap_secret** | **str** | Target Encrypted Chap Secret | [optional] 
**ua_rep_lun** | **bool** | Indicates if the UaRepLun is enabled or not | [optional] 
**uri** | **str** | Resoure Uri of the Host | [optional] 

## Example

```python
from dscc.models.device_type4_host_list_obj import DeviceType4HostListObj

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostListObj from a JSON string
device_type4_host_list_obj_instance = DeviceType4HostListObj.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostListObj.to_json())

# convert the object into a dict
device_type4_host_list_obj_dict = device_type4_host_list_obj_instance.to_dict()
# create an instance of DeviceType4HostListObj from a dict
device_type4_host_list_obj_from_dict = DeviceType4HostListObj.from_dict(device_type4_host_list_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


