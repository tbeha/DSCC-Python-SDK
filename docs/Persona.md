# Persona

Host Persona

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **List[Optional[str]]** |  | [optional] 
**id** | **int** | Numeric ID of the resource | [optional] 
**name** | **str** | Host Name | [optional] 

## Example

```python
from dscc.models.persona import Persona

# TODO update the JSON string below
json = "{}"
# create an instance of Persona from a JSON string
persona_instance = Persona.from_json(json)
# print the JSON string representation of the object
print(Persona.to_json())

# convert the object into a dict
persona_dict = persona_instance.to_dict()
# create an instance of Persona from a dict
persona_from_dict = Persona.from_dict(persona_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


