# DeviceType4ChangeProximitySettingsInput

Request body to change proximity settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[DeviceType4HostProximityInput]**](DeviceType4HostProximityInput.md) |  | 

## Example

```python
from dscc.models.device_type4_change_proximity_settings_input import DeviceType4ChangeProximitySettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ChangeProximitySettingsInput from a JSON string
device_type4_change_proximity_settings_input_instance = DeviceType4ChangeProximitySettingsInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ChangeProximitySettingsInput.to_json())

# convert the object into a dict
device_type4_change_proximity_settings_input_dict = device_type4_change_proximity_settings_input_instance.to_dict()
# create an instance of DeviceType4ChangeProximitySettingsInput from a dict
device_type4_change_proximity_settings_input_from_dict = DeviceType4ChangeProximitySettingsInput.from_dict(device_type4_change_proximity_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


