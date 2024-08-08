# VasaServiceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_mgmt** | **str** | Specify the cert mode for vasa provider, supports values either server or locked_client | [optional] 
**vasa_state_enabled** | **bool** | Specify the status of vasa service. | [optional] 

## Example

```python
from dscc.models.vasa_service_config import VasaServiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VasaServiceConfig from a JSON string
vasa_service_config_instance = VasaServiceConfig.from_json(json)
# print the JSON string representation of the object
print(VasaServiceConfig.to_json())

# convert the object into a dict
vasa_service_config_dict = vasa_service_config_instance.to_dict()
# create an instance of VasaServiceConfig from a dict
vasa_service_config_from_dict = VasaServiceConfig.from_dict(vasa_service_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


