# NimbleFCTargetInfo

Information about the Fibre Channel target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_fcid** | **str** | FCID assigned to the Fibre Channel target port. | [optional] 
**target_port_array_name** | **str** | Name of the array hosting the Fibre Channel target port. | [optional] 
**target_port_ctrlr_name** | **str** | Name (A or B) of the controller to which the port belongs. | [optional] 
**target_port_interface_name** | **str** | Name of the interface hosted on the Fibre Channel target port. | [optional] 
**target_wwnn** | **str** | WWNN (World Wide Node Name) of the Fibre Channel target port. | [optional] 
**target_wwpn** | **str** | WWPN (World Wide Port Name) of the Fibre Channel target port. | [optional] 

## Example

```python
from dscc.models.nimble_fc_target_info import NimbleFCTargetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFCTargetInfo from a JSON string
nimble_fc_target_info_instance = NimbleFCTargetInfo.from_json(json)
# print the JSON string representation of the object
print(NimbleFCTargetInfo.to_json())

# convert the object into a dict
nimble_fc_target_info_dict = nimble_fc_target_info_instance.to_dict()
# create an instance of NimbleFCTargetInfo from a dict
nimble_fc_target_info_from_dict = NimbleFCTargetInfo.from_dict(nimble_fc_target_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


