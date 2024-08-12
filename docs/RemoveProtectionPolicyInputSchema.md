# RemoveProtectionPolicyInputSchema

Protection policy to be removed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote** | [**RemoveRemoteProtectionInputSchema**](RemoveRemoteProtectionInputSchema.md) | Remote protection to be removed | [optional] 
**remove_only_schedules** | **bool** | Remove only schedules and retain remote protection | [optional] 
**remove_schedules** | [**List[RemoveProtectionScheduleInputSchema]**](RemoveProtectionScheduleInputSchema.md) | List of protection schedules to be removed | [optional] 
**secondary_remote** | [**RemoveRemoteProtectionInputSchema**](RemoveRemoteProtectionInputSchema.md) | Secondary remote protection to be removed | [optional] 

## Example

```python
from dscc.models.remove_protection_policy_input_schema import RemoveProtectionPolicyInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveProtectionPolicyInputSchema from a JSON string
remove_protection_policy_input_schema_instance = RemoveProtectionPolicyInputSchema.from_json(json)
# print the JSON string representation of the object
print(RemoveProtectionPolicyInputSchema.to_json())

# convert the object into a dict
remove_protection_policy_input_schema_dict = remove_protection_policy_input_schema_instance.to_dict()
# create an instance of RemoveProtectionPolicyInputSchema from a dict
remove_protection_policy_input_schema_from_dict = RemoveProtectionPolicyInputSchema.from_dict(remove_protection_policy_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


