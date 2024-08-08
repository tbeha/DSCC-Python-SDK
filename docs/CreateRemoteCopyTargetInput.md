# CreateRemoteCopyTargetInput

Request body for creating remote copy targets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Enable (true) or disable (false) the creation of the target in disabled mode | [optional] 
**name** | **str** | Name of the remote copy target | 
**node_wwn** | **str** | WWN of the node on the target system for FC Link type. Ignored if specified for IP type. | [optional] 
**port_pos_and_link** | [**List[PortPosAndLinkInput]**](PortPosAndLinkInput.md) | Specifies all locations (portPos) of the local system, and all links(IP or WWN) of the remote system | 
**type** | **int** | Specifies the link protocol. Do not use UNKNOWN as a linkType enumeration value when creating a Remote Copy target. 1 for IP Target Type, 2 for FC Target Type | 

## Example

```python
from dscc.models.create_remote_copy_target_input import CreateRemoteCopyTargetInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRemoteCopyTargetInput from a JSON string
create_remote_copy_target_input_instance = CreateRemoteCopyTargetInput.from_json(json)
# print the JSON string representation of the object
print(CreateRemoteCopyTargetInput.to_json())

# convert the object into a dict
create_remote_copy_target_input_dict = create_remote_copy_target_input_instance.to_dict()
# create an instance of CreateRemoteCopyTargetInput from a dict
create_remote_copy_target_input_from_dict = CreateRemoteCopyTargetInput.from_dict(create_remote_copy_target_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


