# AttachDetachInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Attach or Detach action name | [optional] 
**parameter** | [**AttachDetachInputParameter**](AttachDetachInputParameter.md) |  | [optional] 

## Example

```python
from dscc.models.attach_detach_input import AttachDetachInput

# TODO update the JSON string below
json = "{}"
# create an instance of AttachDetachInput from a JSON string
attach_detach_input_instance = AttachDetachInput.from_json(json)
# print the JSON string representation of the object
print(AttachDetachInput.to_json())

# convert the object into a dict
attach_detach_input_dict = attach_detach_input_instance.to_dict()
# create an instance of AttachDetachInput from a dict
attach_detach_input_from_dict = AttachDetachInput.from_dict(attach_detach_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


