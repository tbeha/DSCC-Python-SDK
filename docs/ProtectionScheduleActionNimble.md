# ProtectionScheduleActionNimble

Protection Schedule input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the protection schedule. A 42 digit hexadecimal number. | [optional] 

## Example

```python
from dscc.models.protection_schedule_action_nimble import ProtectionScheduleActionNimble

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionScheduleActionNimble from a JSON string
protection_schedule_action_nimble_instance = ProtectionScheduleActionNimble.from_json(json)
# print the JSON string representation of the object
print(ProtectionScheduleActionNimble.to_json())

# convert the object into a dict
protection_schedule_action_nimble_dict = protection_schedule_action_nimble_instance.to_dict()
# create an instance of ProtectionScheduleActionNimble from a dict
protection_schedule_action_nimble_from_dict = ProtectionScheduleActionNimble.from_dict(protection_schedule_action_nimble_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


