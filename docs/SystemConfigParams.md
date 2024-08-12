# SystemConfigParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**SystemSettingsDetails**](SystemSettingsDetails.md) |  | [optional] 
**request_uri** | **str** | requestUri for system settings details | [optional] 

## Example

```python
from dscc.models.system_config_params import SystemConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigParams from a JSON string
system_config_params_instance = SystemConfigParams.from_json(json)
# print the JSON string representation of the object
print(SystemConfigParams.to_json())

# convert the object into a dict
system_config_params_dict = system_config_params_instance.to_dict()
# create an instance of SystemConfigParams from a dict
system_config_params_from_dict = SystemConfigParams.from_dict(system_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


