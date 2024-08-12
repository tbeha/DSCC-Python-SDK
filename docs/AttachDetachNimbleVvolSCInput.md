# AttachDetachNimbleVvolSCInput

Request body to attach VMware Storage Container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Attach action name | [optional] 
**host_initiator_group_ids** | **List[str]** | List of Host Initiator group IDs | [optional] 
**host_initiators_ids** | **List[str]** | List of Host Initiator IDs | [optional] 

## Example

```python
from dscc.models.attach_detach_nimble_vvol_sc_input import AttachDetachNimbleVvolSCInput

# TODO update the JSON string below
json = "{}"
# create an instance of AttachDetachNimbleVvolSCInput from a JSON string
attach_detach_nimble_vvol_sc_input_instance = AttachDetachNimbleVvolSCInput.from_json(json)
# print the JSON string representation of the object
print(AttachDetachNimbleVvolSCInput.to_json())

# convert the object into a dict
attach_detach_nimble_vvol_sc_input_dict = attach_detach_nimble_vvol_sc_input_instance.to_dict()
# create an instance of AttachDetachNimbleVvolSCInput from a dict
attach_detach_nimble_vvol_sc_input_from_dict = AttachDetachNimbleVvolSCInput.from_dict(attach_detach_nimble_vvol_sc_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


