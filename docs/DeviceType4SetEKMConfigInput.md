# DeviceType4SetEKMConfigInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**DeviceType4SetEKMConfigParams**](DeviceType4SetEKMConfigParams.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_set_ekm_config_input import DeviceType4SetEKMConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SetEKMConfigInput from a JSON string
device_type4_set_ekm_config_input_instance = DeviceType4SetEKMConfigInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SetEKMConfigInput.to_json())

# convert the object into a dict
device_type4_set_ekm_config_input_dict = device_type4_set_ekm_config_input_instance.to_dict()
# create an instance of DeviceType4SetEKMConfigInput from a dict
device_type4_set_ekm_config_input_from_dict = DeviceType4SetEKMConfigInput.from_dict(device_type4_set_ekm_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


