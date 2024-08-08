# SetEKMConfigParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ekmpassword** | **str** | Password for External Key Manager. | [optional] 
**ekmuser** | **str** | Username on External Key Manager. | [optional] 
**kmipprotocols** | **List[str]** | KMIP protocol. | [optional] 
**port** | **str** | Connection port number for External Key Managers. | [optional] 
**serverlist** | **List[str]** | List of External Key Management servers. | [optional] 

## Example

```python
from dscc.models.set_ekm_config_params import SetEKMConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of SetEKMConfigParams from a JSON string
set_ekm_config_params_instance = SetEKMConfigParams.from_json(json)
# print the JSON string representation of the object
print(SetEKMConfigParams.to_json())

# convert the object into a dict
set_ekm_config_params_dict = set_ekm_config_params_instance.to_dict()
# create an instance of SetEKMConfigParams from a dict
set_ekm_config_params_from_dict = SetEKMConfigParams.from_dict(set_ekm_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


