# NimbleFCInitiatorInfo

Information about the Fibre Channel initiator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator_alias** | **str** | Alias of the Fibre Channel initiator. | [optional] 
**initiator_fcid** | **str** | FCID assigned to the Fibre Channel initiator. | [optional] 
**initiator_switch_name** | **str** | Name of the switch used by the Fibre Channel initiator. | [optional] 
**initiator_switch_port** | **str** | Port on the switch used by the Fibre Channel initiator. | [optional] 
**initiator_symbolic_nodename** | **str** | Symbolic node name associated with the Fibre Channel initiator. | [optional] 
**initiator_symbolic_portname** | **str** | Symbolic port name associated with the Fibre Channel initiator. | [optional] 
**initiator_wwpn** | **str** | WWPN (World Wide Port Name) of the Fibre Channel initiator. | [optional] 

## Example

```python
from dscc.models.nimble_fc_initiator_info import NimbleFCInitiatorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFCInitiatorInfo from a JSON string
nimble_fc_initiator_info_instance = NimbleFCInitiatorInfo.from_json(json)
# print the JSON string representation of the object
print(NimbleFCInitiatorInfo.to_json())

# convert the object into a dict
nimble_fc_initiator_info_dict = nimble_fc_initiator_info_instance.to_dict()
# create an instance of NimbleFCInitiatorInfo from a dict
nimble_fc_initiator_info_from_dict = NimbleFCInitiatorInfo.from_dict(nimble_fc_initiator_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


