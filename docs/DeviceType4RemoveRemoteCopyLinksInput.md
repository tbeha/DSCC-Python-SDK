# DeviceType4RemoveRemoteCopyLinksInput

Request Body for removing remote copy links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partner_system_id** | **str** | SystemId of target replication partner | 
**source** | [**List[DeviceType4RCLinkId]**](DeviceType4RCLinkId.md) | List of remote copy links to be deleted from source replication partner | 
**target** | [**List[DeviceType4RCLinkId]**](DeviceType4RCLinkId.md) | List of remote copy links to be deleted from target replication partner | 

## Example

```python
from dscc.models.device_type4_remove_remote_copy_links_input import DeviceType4RemoveRemoteCopyLinksInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RemoveRemoteCopyLinksInput from a JSON string
device_type4_remove_remote_copy_links_input_instance = DeviceType4RemoveRemoteCopyLinksInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RemoveRemoteCopyLinksInput.to_json())

# convert the object into a dict
device_type4_remove_remote_copy_links_input_dict = device_type4_remove_remote_copy_links_input_instance.to_dict()
# create an instance of DeviceType4RemoveRemoteCopyLinksInput from a dict
device_type4_remove_remote_copy_links_input_from_dict = DeviceType4RemoveRemoteCopyLinksInput.from_dict(device_type4_remove_remote_copy_links_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


