# EditProtectionPolicyInputSchema

Request body for edit protection policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_schedules** | [**List[PrimeraProtectionScheduleInputSchema]**](PrimeraProtectionScheduleInputSchema.md) |  | [optional] 
**modify_schedules** | [**List[ModifyProtectionScheduleInputSchema]**](ModifyProtectionScheduleInputSchema.md) |  | [optional] 
**policy** | [**PrimeraProtectionPolicyInputSchema**](PrimeraProtectionPolicyInputSchema.md) |  | [optional] 
**protection_policy_type** | **str** | Specifies Protection policy type. Synchronous replication/protection policy provides protection from array or site failures with zero RPO. Using this policy, you can also configure zero RTO policy like Active Peer Persistence. Asynchronous replication/protection policy provides protection from array or site failure with the user defined RPO.  Schedule snapshot policy takes snapshots of the member volumes of the protected volume set at periodic intervals defined by the user. You can setup the local snapshot schedule and also setup the co-ordinated synchronized snapshot schedule on the protected volume set configured with synchronous or asynchronous replication policy. You can do this by attaching a scheduled snapshot policy on the volume set having already a synchronous or asynchronous protecting policy. | 
**remove_schedules** | [**List[RemoveProtectionScheduleInputSchema]**](RemoveProtectionScheduleInputSchema.md) |  | [optional] 

## Example

```python
from dscc.models.edit_protection_policy_input_schema import EditProtectionPolicyInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EditProtectionPolicyInputSchema from a JSON string
edit_protection_policy_input_schema_instance = EditProtectionPolicyInputSchema.from_json(json)
# print the JSON string representation of the object
print(EditProtectionPolicyInputSchema.to_json())

# convert the object into a dict
edit_protection_policy_input_schema_dict = edit_protection_policy_input_schema_instance.to_dict()
# create an instance of EditProtectionPolicyInputSchema from a dict
edit_protection_policy_input_schema_from_dict = EditProtectionPolicyInputSchema.from_dict(edit_protection_policy_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


