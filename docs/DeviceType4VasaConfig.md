# DeviceType4VasaConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specify the action on vasa service. Either START, STOP or RESET | [optional] 

## Example

```python
from dscc.models.device_type4_vasa_config import DeviceType4VasaConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4VasaConfig from a JSON string
device_type4_vasa_config_instance = DeviceType4VasaConfig.from_json(json)
# print the JSON string representation of the object
print(DeviceType4VasaConfig.to_json())

# convert the object into a dict
device_type4_vasa_config_dict = device_type4_vasa_config_instance.to_dict()
# create an instance of DeviceType4VasaConfig from a dict
device_type4_vasa_config_from_dict = DeviceType4VasaConfig.from_dict(device_type4_vasa_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


