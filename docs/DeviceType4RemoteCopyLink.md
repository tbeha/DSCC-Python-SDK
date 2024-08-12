# DeviceType4RemoteCopyLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipc** | **str** | Name given to the link IPC. | [optional] 
**display_name** | **str** | Replication partner link displayname. | [optional] 
**domain** | **str** | Domain that the resource belongs to. | [optional] 
**id** | **str** | Unique Identifier of the link | [optional] 
**name** | **str** | Replication partner link name. | [optional] 
**partner_name** | **str** | Partner name with which the link is affiliated. | [optional] 
**port** | **str** | Port number. | [optional] 
**port_pos** | [**DeviceType4RemoteCopyLinkPortPosition**](DeviceType4RemoteCopyLinkPortPosition.md) | Port position of the link | [optional] 
**rc_link_id** | **int** | Id of the replication partner link. | [optional] 
**remote_address** | **str** | IP address or WWN of the remote link. | [optional] 
**remote_id** | **str** | Unique Identifier of the remote partner link | [optional] 
**remote_port_pos** | [**DeviceType4RemoteCopyLinkPortPosition**](DeviceType4RemoteCopyLinkPortPosition.md) | Port position of the remote link | [optional] 
**remote_state** | **str** | state of the remote replicatoin partner link. | [optional] 
**remote_status** | **str** | status of the remote replication partner link. | [optional] 
**source_address** | **str** | IP address or WWN of the link. | [optional] 
**state** | **str** | state of the replication partner link. | [optional] 
**status** | **str** | status of the replication partner link. | [optional] 
**system_id** | **str** | Unique ID or serial number of the system. | [optional] 
**system_wwn** | **str** | WWN of the system. | [optional] 
**throughput_k_byte_sec** | **int** | Link throughput in KBytes/sec. | [optional] 
**type** | **int** | Link type IP or FC. | [optional] 

## Example

```python
from dscc.models.device_type4_remote_copy_link import DeviceType4RemoteCopyLink

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RemoteCopyLink from a JSON string
device_type4_remote_copy_link_instance = DeviceType4RemoteCopyLink.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RemoteCopyLink.to_json())

# convert the object into a dict
device_type4_remote_copy_link_dict = device_type4_remote_copy_link_instance.to_dict()
# create an instance of DeviceType4RemoteCopyLink from a dict
device_type4_remote_copy_link_from_dict = DeviceType4RemoteCopyLink.from_dict(device_type4_remote_copy_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


