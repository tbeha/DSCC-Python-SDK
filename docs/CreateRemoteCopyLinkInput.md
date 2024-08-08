# CreateRemoteCopyLinkInput

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
from dscc.models.create_remote_copy_link_input import CreateRemoteCopyLinkInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRemoteCopyLinkInput from a JSON string
create_remote_copy_link_input_instance = CreateRemoteCopyLinkInput.from_json(json)
# print the JSON string representation of the object
print(CreateRemoteCopyLinkInput.to_json())

# convert the object into a dict
create_remote_copy_link_input_dict = create_remote_copy_link_input_instance.to_dict()
# create an instance of CreateRemoteCopyLinkInput from a dict
create_remote_copy_link_input_from_dict = CreateRemoteCopyLinkInput.from_dict(create_remote_copy_link_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


