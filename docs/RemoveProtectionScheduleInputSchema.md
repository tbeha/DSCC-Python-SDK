# RemoveProtectionScheduleInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Protection schedule ID | 

## Example

```python
from dscc.models.remove_protection_schedule_input_schema import RemoveProtectionScheduleInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveProtectionScheduleInputSchema from a JSON string
remove_protection_schedule_input_schema_instance = RemoveProtectionScheduleInputSchema.from_json(json)
# print the JSON string representation of the object
print(RemoveProtectionScheduleInputSchema.to_json())

# convert the object into a dict
remove_protection_schedule_input_schema_dict = remove_protection_schedule_input_schema_instance.to_dict()
# create an instance of RemoveProtectionScheduleInputSchema from a dict
remove_protection_schedule_input_schema_from_dict = RemoveProtectionScheduleInputSchema.from_dict(remove_protection_schedule_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


