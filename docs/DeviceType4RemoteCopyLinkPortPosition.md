# DeviceType4RemoteCopyLinkPortPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **int** | Port position node number | [optional] 
**port** | **int** | Port position port number | [optional] 
**slot** | **int** | Port position slot number | [optional] 

## Example

```python
from dscc.models.device_type4_remote_copy_link_port_position import DeviceType4RemoteCopyLinkPortPosition

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RemoteCopyLinkPortPosition from a JSON string
device_type4_remote_copy_link_port_position_instance = DeviceType4RemoteCopyLinkPortPosition.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RemoteCopyLinkPortPosition.to_json())

# convert the object into a dict
device_type4_remote_copy_link_port_position_dict = device_type4_remote_copy_link_port_position_instance.to_dict()
# create an instance of DeviceType4RemoteCopyLinkPortPosition from a dict
device_type4_remote_copy_link_port_position_from_dict = DeviceType4RemoteCopyLinkPortPosition.from_dict(device_type4_remote_copy_link_port_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


