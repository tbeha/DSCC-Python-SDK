# DeviceType4RemoteCopyLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4RemoteCopyLink]**](DeviceType4RemoteCopyLink.md) |  | [optional] 
**total** | **int** | Total number of remote partner links. | [optional] 

## Example

```python
from dscc.models.device_type4_remote_copy_links import DeviceType4RemoteCopyLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RemoteCopyLinks from a JSON string
device_type4_remote_copy_links_instance = DeviceType4RemoteCopyLinks.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RemoteCopyLinks.to_json())

# convert the object into a dict
device_type4_remote_copy_links_dict = device_type4_remote_copy_links_instance.to_dict()
# create an instance of DeviceType4RemoteCopyLinks from a dict
device_type4_remote_copy_links_from_dict = DeviceType4RemoteCopyLinks.from_dict(device_type4_remote_copy_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


