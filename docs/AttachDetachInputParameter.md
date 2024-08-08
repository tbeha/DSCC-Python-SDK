# AttachDetachInputParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Attach or Detach action name | [optional] 
**host_ids** | **List[str]** | Host IDs | [optional] 
**host_set_ids** | **List[str]** | Host Set IDs | [optional] 

## Example

```python
from dscc.models.attach_detach_input_parameter import AttachDetachInputParameter

# TODO update the JSON string below
json = "{}"
# create an instance of AttachDetachInputParameter from a JSON string
attach_detach_input_parameter_instance = AttachDetachInputParameter.from_json(json)
# print the JSON string representation of the object
print(AttachDetachInputParameter.to_json())

# convert the object into a dict
attach_detach_input_parameter_dict = attach_detach_input_parameter_instance.to_dict()
# create an instance of AttachDetachInputParameter from a dict
attach_detach_input_parameter_from_dict = AttachDetachInputParameter.from_dict(attach_detach_input_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


