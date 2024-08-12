# ChangeProximitySettingsInput

Request body to change proximity settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[HostProximityInput]**](HostProximityInput.md) |  | 

## Example

```python
from dscc.models.change_proximity_settings_input import ChangeProximitySettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeProximitySettingsInput from a JSON string
change_proximity_settings_input_instance = ChangeProximitySettingsInput.from_json(json)
# print the JSON string representation of the object
print(ChangeProximitySettingsInput.to_json())

# convert the object into a dict
change_proximity_settings_input_dict = change_proximity_settings_input_instance.to_dict()
# create an instance of ChangeProximitySettingsInput from a dict
change_proximity_settings_input_from_dict = ChangeProximitySettingsInput.from_dict(change_proximity_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


