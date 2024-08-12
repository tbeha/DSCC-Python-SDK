# DeviceType4CreateRemoteCopyLinkInput

Request body for creating remote copy links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | IP Address or WWN of Remote Copy target for this link, depending on the link type IP or FC | 
**port_pos** | [**CreateRemoteCopyLinkInputPortPos**](CreateRemoteCopyLinkInputPortPos.md) |  | 
**target_name** | **str** | Remote Copy target with which the link is affiliated | 
**type** | **int** | Remote Copy link type. 1 for IP and 2 for FC | 

## Example

```python
from dscc.models.device_type4_create_remote_copy_link_input import DeviceType4CreateRemoteCopyLinkInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CreateRemoteCopyLinkInput from a JSON string
device_type4_create_remote_copy_link_input_instance = DeviceType4CreateRemoteCopyLinkInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CreateRemoteCopyLinkInput.to_json())

# convert the object into a dict
device_type4_create_remote_copy_link_input_dict = device_type4_create_remote_copy_link_input_instance.to_dict()
# create an instance of DeviceType4CreateRemoteCopyLinkInput from a dict
device_type4_create_remote_copy_link_input_from_dict = DeviceType4CreateRemoteCopyLinkInput.from_dict(device_type4_create_remote_copy_link_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


