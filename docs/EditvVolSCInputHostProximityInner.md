# EditvVolSCInputHostProximityInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Host names which are exporting a remote copy group | [optional] 
**proximity** | **str** | Host Proximity to be set | [optional] 
**rcopy_group** | **List[str]** | List of rcopy group names to set the host proximity | [optional] 

## Example

```python
from dscc.models.editv_vol_sc_input_host_proximity_inner import EditvVolSCInputHostProximityInner

# TODO update the JSON string below
json = "{}"
# create an instance of EditvVolSCInputHostProximityInner from a JSON string
editv_vol_sc_input_host_proximity_inner_instance = EditvVolSCInputHostProximityInner.from_json(json)
# print the JSON string representation of the object
print(EditvVolSCInputHostProximityInner.to_json())

# convert the object into a dict
editv_vol_sc_input_host_proximity_inner_dict = editv_vol_sc_input_host_proximity_inner_instance.to_dict()
# create an instance of EditvVolSCInputHostProximityInner from a dict
editv_vol_sc_input_host_proximity_inner_from_dict = EditvVolSCInputHostProximityInner.from_dict(editv_vol_sc_input_host_proximity_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


