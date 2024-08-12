# VasaConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specify the action on vasa service. Either START, STOP or RESET | [optional] 

## Example

```python
from dscc.models.vasa_config import VasaConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VasaConfig from a JSON string
vasa_config_instance = VasaConfig.from_json(json)
# print the JSON string representation of the object
print(VasaConfig.to_json())

# convert the object into a dict
vasa_config_dict = vasa_config_instance.to_dict()
# create an instance of VasaConfig from a dict
vasa_config_from_dict = VasaConfig.from_dict(vasa_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


