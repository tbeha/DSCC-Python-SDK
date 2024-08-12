# DeviceType4VasaServiceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_mgmt** | **str** | Specify the cert mode for vasa provider, supports values server, locked_client or multi_vc. multi_vc is supported from OS version 10.4.0 and Vasa version 5.0.0.0 | [optional] 
**vasa_state_enabled** | **bool** | Specify the status of vasa service. | [optional] 

## Example

```python
from dscc.models.device_type4_vasa_service_config import DeviceType4VasaServiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VasaServiceConfig from a JSON string
device_type4_vasa_service_config_instance = DeviceType4VasaServiceConfig.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VasaServiceConfig.to_json())

# convert the object into a dict
device_type4_vasa_service_config_dict = device_type4_vasa_service_config_instance.to_dict()
# create an instance of DeviceType4VasaServiceConfig from a dict
device_type4_vasa_service_config_from_dict = DeviceType4VasaServiceConfig.from_dict(device_type4_vasa_service_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


