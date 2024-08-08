# AddRemoteCopyLinks

Request body for adding remote copy links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partner_system_id** | **str** | SystemId of target replication partner | 
**source** | [**List[CreateRemoteCopyLinkInput]**](CreateRemoteCopyLinkInput.md) | List of remote copy links to be added to source replication partner | 
**target** | [**List[CreateRemoteCopyLinkInput]**](CreateRemoteCopyLinkInput.md) | List of remote copy links to be added to target replication partner | 

## Example

```python
from dscc.models.add_remote_copy_links import AddRemoteCopyLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AddRemoteCopyLinks from a JSON string
add_remote_copy_links_instance = AddRemoteCopyLinks.from_json(json)
# print the JSON string representation of the object
print(AddRemoteCopyLinks.to_json())

# convert the object into a dict
add_remote_copy_links_dict = add_remote_copy_links_instance.to_dict()
# create an instance of AddRemoteCopyLinks from a dict
add_remote_copy_links_from_dict = AddRemoteCopyLinks.from_dict(add_remote_copy_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


