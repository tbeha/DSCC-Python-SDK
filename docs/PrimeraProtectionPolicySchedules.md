# PrimeraProtectionPolicySchedules

Schedules on application set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PrimeraSchedule]**](PrimeraSchedule.md) |  | [optional] 
**total** | **int** | Number of schedules on application set | [optional] 

## Example

```python
from dscc.models.primera_protection_policy_schedules import PrimeraProtectionPolicySchedules

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraProtectionPolicySchedules from a JSON string
primera_protection_policy_schedules_instance = PrimeraProtectionPolicySchedules.from_json(json)
# print the JSON string representation of the object
print(PrimeraProtectionPolicySchedules.to_json())

# convert the object into a dict
primera_protection_policy_schedules_dict = primera_protection_policy_schedules_instance.to_dict()
# create an instance of PrimeraProtectionPolicySchedules from a dict
primera_protection_policy_schedules_from_dict = PrimeraProtectionPolicySchedules.from_dict(primera_protection_policy_schedules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


