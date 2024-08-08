# PortFCEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_mode** | **str** | Configuration of Port. Possible Values: Disk, Host, RCFC, Peer | [optional] 
**connection_type** | **str** | Port connection Type. Possible Values: Point, Loop | [optional] 
**interupt_coalesce** | **bool** | Port interuptCoalesce enabled or not | [optional] 
**label** | **str** | Port name | [optional] 
**speed_configured** | **str** | Port speed. Possible Values: auto, \&quot;4\&quot;, \&quot;8\&quot;, \&quot;16\&quot;, \&quot;32\&quot; | [optional] 
**unique_wwn** | **bool** | Port uniquewwn enabled or not | [optional] 
**vcn** | **bool** | VLUN change notification enabled or not | [optional] 

## Example

```python
from dscc.models.port_fc_edit import PortFCEdit

# TODO update the JSON string below
json = "{}"
# create an instance of PortFCEdit from a JSON string
port_fc_edit_instance = PortFCEdit.from_json(json)
# print the JSON string representation of the object
print(PortFCEdit.to_json())

# convert the object into a dict
port_fc_edit_dict = port_fc_edit_instance.to_dict()
# create an instance of PortFCEdit from a dict
port_fc_edit_from_dict = PortFCEdit.from_dict(port_fc_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


