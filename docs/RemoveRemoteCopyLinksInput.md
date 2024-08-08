# RemoveRemoteCopyLinksInput

Request Body for removing remote copy links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partner_system_id** | **str** | SystemId of target replication partner | 
**source** | [**List[RCLinkId]**](RCLinkId.md) | List of remote copy links to be deleted from source replication partner | 
**target** | [**List[RCLinkId]**](RCLinkId.md) | List of remote copy links to be deleted from target replication partner | 

## Example

```python
from dscc.models.remove_remote_copy_links_input import RemoveRemoteCopyLinksInput

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveRemoteCopyLinksInput from a JSON string
remove_remote_copy_links_input_instance = RemoveRemoteCopyLinksInput.from_json(json)
# print the JSON string representation of the object
print(RemoveRemoteCopyLinksInput.to_json())

# convert the object into a dict
remove_remote_copy_links_input_dict = remove_remote_copy_links_input_instance.to_dict()
# create an instance of RemoveRemoteCopyLinksInput from a dict
remove_remote_copy_links_input_from_dict = RemoveRemoteCopyLinksInput.from_dict(remove_remote_copy_links_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


