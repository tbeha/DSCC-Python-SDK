# NimbleFCInitiator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Alias of the Fibre Channel initiator. | [optional] 
**id** | **str** | Unique identifier of the Fibre Channel initiator. | [optional] 
**initiator_id** | **str** | Unique identifier of the Fibre Channel initiator. | [optional] 
**wwpn** | **str** | WWPN (World Wide Port Name) of the Fibre Channel initiator. | [optional] 

## Example

```python
from dscc.models.nimble_fc_initiator import NimbleFCInitiator

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFCInitiator from a JSON string
nimble_fc_initiator_instance = NimbleFCInitiator.from_json(json)
# print the JSON string representation of the object
print(NimbleFCInitiator.to_json())

# convert the object into a dict
nimble_fc_initiator_dict = nimble_fc_initiator_instance.to_dict()
# create an instance of NimbleFCInitiator from a dict
nimble_fc_initiator_from_dict = NimbleFCInitiator.from_dict(nimble_fc_initiator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


