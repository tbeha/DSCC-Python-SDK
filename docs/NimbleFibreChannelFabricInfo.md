# NimbleFibreChannelFabricInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fabric_switch_name** | **str** | Name of the Fibre Channel switch. | [optional] 
**fabric_switch_port** | **int** | Port on the Fibre Channel switch to which connection is established. | [optional] 
**fabric_switch_port_number** | **str** | Port Number on the Fibre Channel switch to which connection is established. | [optional] 
**fabric_switch_wwnn** | **str** | World Wide Node Name for the connected port on the fabric switch. | [optional] 
**fabric_switch_wwpn** | **str** | World Wide Port Name for the connected port on the fabric switch. | [optional] 
**fabric_wwn** | **str** | World Wide Node Name for the Fabric Switch. | [optional] 
**fc_id** | **str** | FCID assigned to the Fabric Channel fabric port. | [optional] 
**logged_in** | **bool** | Login information for interface. True if interface has logged in to the Fibre Channel fabric, else false. | [optional] 

## Example

```python
from dscc.models.nimble_fibre_channel_fabric_info import NimbleFibreChannelFabricInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFibreChannelFabricInfo from a JSON string
nimble_fibre_channel_fabric_info_instance = NimbleFibreChannelFabricInfo.from_json(json)
# print the JSON string representation of the object
print(NimbleFibreChannelFabricInfo.to_json())

# convert the object into a dict
nimble_fibre_channel_fabric_info_dict = nimble_fibre_channel_fabric_info_instance.to_dict()
# create an instance of NimbleFibreChannelFabricInfo from a dict
nimble_fibre_channel_fabric_info_from_dict = NimbleFibreChannelFabricInfo.from_dict(nimble_fibre_channel_fabric_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


