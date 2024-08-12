# PortISCSIEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_address** | **str** | Gateway address to edit to | [optional] 
**ip_address** | **str** | IP address to edit to | [optional] 
**label** | **str** | label of the port to edit to | [optional] 
**mtu** | **str** | MTU to edit to. Possible Values: \&quot;1500\&quot;, \&quot;9000\&quot; | [optional] 
**net_mask** | **str** | NetMask address to edit to | [optional] 
**send_target_group_tag** | **int** |  | [optional] 

## Example

```python
from dscc.models.port_iscsi_edit import PortISCSIEdit

# TODO update the JSON string below
json = "{}"
# create an instance of PortISCSIEdit from a JSON string
port_iscsi_edit_instance = PortISCSIEdit.from_json(json)
# print the JSON string representation of the object
print(PortISCSIEdit.to_json())

# convert the object into a dict
port_iscsi_edit_dict = port_iscsi_edit_instance.to_dict()
# create an instance of PortISCSIEdit from a dict
port_iscsi_edit_from_dict = PortISCSIEdit.from_dict(port_iscsi_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


