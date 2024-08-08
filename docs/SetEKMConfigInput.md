# SetEKMConfigInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**SetEKMConfigParams**](SetEKMConfigParams.md) |  | [optional] 

## Example

```python
from dscc.models.set_ekm_config_input import SetEKMConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of SetEKMConfigInput from a JSON string
set_ekm_config_input_instance = SetEKMConfigInput.from_json(json)
# print the JSON string representation of the object
print(SetEKMConfigInput.to_json())

# convert the object into a dict
set_ekm_config_input_dict = set_ekm_config_input_instance.to_dict()
# create an instance of SetEKMConfigInput from a dict
set_ekm_config_input_from_dict = SetEKMConfigInput.from_dict(set_ekm_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


