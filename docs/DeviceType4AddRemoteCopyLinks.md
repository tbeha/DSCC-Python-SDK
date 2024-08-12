# DeviceType4AddRemoteCopyLinks

Request body for adding remote copy links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partner_system_id** | **str** | SystemId of target replication partner | 
**source** | [**List[DeviceType4CreateRemoteCopyLinkInput]**](DeviceType4CreateRemoteCopyLinkInput.md) | List of remote copy links to be added to source replication partner | 
**target** | [**List[DeviceType4CreateRemoteCopyLinkInput]**](DeviceType4CreateRemoteCopyLinkInput.md) | List of remote copy links to be added to target replication partner | 

## Example

```python
from dscc.models.device_type4_add_remote_copy_links import DeviceType4AddRemoteCopyLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4AddRemoteCopyLinks from a JSON string
device_type4_add_remote_copy_links_instance = DeviceType4AddRemoteCopyLinks.from_json(json)
# print the JSON string representation of the object
print(DeviceType4AddRemoteCopyLinks.to_json())

# convert the object into a dict
device_type4_add_remote_copy_links_dict = device_type4_add_remote_copy_links_instance.to_dict()
# create an instance of DeviceType4AddRemoteCopyLinks from a dict
device_type4_add_remote_copy_links_from_dict = DeviceType4AddRemoteCopyLinks.from_dict(device_type4_add_remote_copy_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


