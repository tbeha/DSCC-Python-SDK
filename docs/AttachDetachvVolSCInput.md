# AttachDetachvVolSCInput

Request body for attaching VMware Storage Container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Attach action name | [optional] 
**host_ids** | **List[str]** | Host IDs | [optional] 
**host_set_ids** | **List[str]** | Host Set IDs | [optional] 

## Example

```python
from dscc.models.attach_detachv_vol_sc_input import AttachDetachvVolSCInput

# TODO update the JSON string below
json = "{}"
# create an instance of AttachDetachvVolSCInput from a JSON string
attach_detachv_vol_sc_input_instance = AttachDetachvVolSCInput.from_json(json)
# print the JSON string representation of the object
print(AttachDetachvVolSCInput.to_json())

# convert the object into a dict
attach_detachv_vol_sc_input_dict = attach_detachv_vol_sc_input_instance.to_dict()
# create an instance of AttachDetachvVolSCInput from a dict
attach_detachv_vol_sc_input_from_dict = AttachDetachvVolSCInput.from_dict(attach_detachv_vol_sc_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


