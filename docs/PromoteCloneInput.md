# PromoteCloneInput

Promote clone input. Promote a clone volume with given priority.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | [**ClonePriority**](ClonePriority.md) |  | [optional] 

## Example

```python
from dscc.models.promote_clone_input import PromoteCloneInput

# TODO update the JSON string below
json = "{}"
# create an instance of PromoteCloneInput from a JSON string
promote_clone_input_instance = PromoteCloneInput.from_json(json)
# print the JSON string representation of the object
print(PromoteCloneInput.to_json())

# convert the object into a dict
promote_clone_input_dict = promote_clone_input_instance.to_dict()
# create an instance of PromoteCloneInput from a dict
promote_clone_input_from_dict = PromoteCloneInput.from_dict(promote_clone_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


