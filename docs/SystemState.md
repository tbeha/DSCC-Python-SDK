# SystemState

State of the resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detailed** | **List[Optional[str]]** | Array of the detailed states of the resource | [optional] 
**overall** | **str** | Overall state of the resource | [optional] 

## Example

```python
from dscc.models.system_state import SystemState

# TODO update the JSON string below
json = "{}"
# create an instance of SystemState from a JSON string
system_state_instance = SystemState.from_json(json)
# print the JSON string representation of the object
print(SystemState.to_json())

# convert the object into a dict
system_state_dict = system_state_instance.to_dict()
# create an instance of SystemState from a dict
system_state_from_dict = SystemState.from_dict(system_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


