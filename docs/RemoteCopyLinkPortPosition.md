# RemoteCopyLinkPortPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** | Port position node number | [optional] 
**port** | **int** | Port position port number | [optional] 
**slot** | **int** | Port position slot number | [optional] 

## Example

```python
from dscc.models.remote_copy_link_port_position import RemoteCopyLinkPortPosition

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteCopyLinkPortPosition from a JSON string
remote_copy_link_port_position_instance = RemoteCopyLinkPortPosition.from_json(json)
# print the JSON string representation of the object
print(RemoteCopyLinkPortPosition.to_json())

# convert the object into a dict
remote_copy_link_port_position_dict = remote_copy_link_port_position_instance.to_dict()
# create an instance of RemoteCopyLinkPortPosition from a dict
remote_copy_link_port_position_from_dict = RemoteCopyLinkPortPosition.from_dict(remote_copy_link_port_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


