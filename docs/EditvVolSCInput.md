# EditvVolSCInput

Request body for editing VMware Storage Container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comments for the object set to be modified | [optional] 
**host_proximity** | [**List[EditvVolSCInputHostProximityInner]**](EditvVolSCInputHostProximityInner.md) | List of member object to set proximity for host and rcopy groups | [optional] 
**members** | **List[str]** | List of members of the object set to be modified | [optional] 
**name** | **str** | Storage Container Name. | [optional] 

## Example

```python
from dscc.models.editv_vol_sc_input import EditvVolSCInput

# TODO update the JSON string below
json = "{}"
# create an instance of EditvVolSCInput from a JSON string
editv_vol_sc_input_instance = EditvVolSCInput.from_json(json)
# print the JSON string representation of the object
print(EditvVolSCInput.to_json())

# convert the object into a dict
editv_vol_sc_input_dict = editv_vol_sc_input_instance.to_dict()
# create an instance of EditvVolSCInput from a dict
editv_vol_sc_input_from_dict = EditvVolSCInput.from_dict(editv_vol_sc_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


