# PrimeraProtectionPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**policy** | [**PrimeraProtectionPolicyPolicy**](PrimeraProtectionPolicyPolicy.md) |  | [optional] 
**protection_policy_type** | **str** | Protection policy type: schedule, sync or async | [optional] 
**schedules** | [**PrimeraProtectionPolicySchedules**](PrimeraProtectionPolicySchedules.md) |  | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.primera_protection_policy import PrimeraProtectionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraProtectionPolicy from a JSON string
primera_protection_policy_instance = PrimeraProtectionPolicy.from_json(json)
# print the JSON string representation of the object
print(PrimeraProtectionPolicy.to_json())

# convert the object into a dict
primera_protection_policy_dict = primera_protection_policy_instance.to_dict()
# create an instance of PrimeraProtectionPolicy from a dict
primera_protection_policy_from_dict = PrimeraProtectionPolicy.from_dict(primera_protection_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


