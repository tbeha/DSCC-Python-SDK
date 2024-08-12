# DeviceType4Persona

Host Persona

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **List[Optional[str]]** |  | [optional] 
**id** | **int** | Numeric ID of the resource | [optional] 
**name** | **str** | Host Name | [optional] 

## Example

```python
from dscc.models.device_type4_persona import DeviceType4Persona

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4Persona from a JSON string
device_type4_persona_instance = DeviceType4Persona.from_json(json)
# print the JSON string representation of the object
print(DeviceType4Persona.to_json())

# convert the object into a dict
device_type4_persona_dict = device_type4_persona_instance.to_dict()
# create an instance of DeviceType4Persona from a dict
device_type4_persona_from_dict = DeviceType4Persona.from_dict(device_type4_persona_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


