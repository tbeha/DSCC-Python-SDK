# PortPosAndLinkInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | Specifies the link for the remote system. If the Link Protocol Type is IP, specify an IP address for the corresponding port on the remote system. If the Link Protocol Type is FC, specify the WWN of the peer port on the remote system | 
**port_position** | [**PortPositionInput**](PortPositionInput.md) |  | 

## Example

```python
from dscc.models.port_pos_and_link_input import PortPosAndLinkInput

# TODO update the JSON string below
json = "{}"
# create an instance of PortPosAndLinkInput from a JSON string
port_pos_and_link_input_instance = PortPosAndLinkInput.from_json(json)
# print the JSON string representation of the object
print(PortPosAndLinkInput.to_json())

# convert the object into a dict
port_pos_and_link_input_dict = port_pos_and_link_input_instance.to_dict()
# create an instance of PortPosAndLinkInput from a dict
port_pos_and_link_input_from_dict = PortPosAndLinkInput.from_dict(port_pos_and_link_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


