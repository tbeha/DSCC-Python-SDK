# State

State of the resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detailed** | **List[Optional[str]]** | Array of the detailed states of the resource | [optional] 
**overall** | **str** | Overall state of the resource | [optional] 

## Example

```python
from dscc.models.state import State

# TODO update the JSON string below
json = "{}"
# create an instance of State from a JSON string
state_instance = State.from_json(json)
# print the JSON string representation of the object
print(State.to_json())

# convert the object into a dict
state_dict = state_instance.to_dict()
# create an instance of State from a dict
state_from_dict = State.from_dict(state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


