# CreateRemoteCopyLinkInputPortPos

Location (node, slot and port) of this link. For IP links, to be created with just node then the slot and port positions will be empty

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** | Port position node number | 
**port** | **int** | Port position port number | 
**slot** | **int** | Port position slot number | 

## Example

```python
from dscc.models.create_remote_copy_link_input_port_pos import CreateRemoteCopyLinkInputPortPos

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRemoteCopyLinkInputPortPos from a JSON string
create_remote_copy_link_input_port_pos_instance = CreateRemoteCopyLinkInputPortPos.from_json(json)
# print the JSON string representation of the object
print(CreateRemoteCopyLinkInputPortPos.to_json())

# convert the object into a dict
create_remote_copy_link_input_port_pos_dict = create_remote_copy_link_input_port_pos_instance.to_dict()
# create an instance of CreateRemoteCopyLinkInputPortPos from a dict
create_remote_copy_link_input_port_pos_from_dict = CreateRemoteCopyLinkInputPortPos.from_dict(create_remote_copy_link_input_port_pos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


