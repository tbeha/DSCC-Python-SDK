# ProtectionPolicySecondaryRemoteInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** | Remote partner ID | 
**partner_name** | **str** | Remote partner name | 
**replication_type** | **str** | Replication type. Supported type is periodic only. Periodic replication (Asynchronous protection policy) provides protection from array or site failure with the user defined RPO. | 

## Example

```python
from dscc.models.protection_policy_secondary_remote_input_schema import ProtectionPolicySecondaryRemoteInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionPolicySecondaryRemoteInputSchema from a JSON string
protection_policy_secondary_remote_input_schema_instance = ProtectionPolicySecondaryRemoteInputSchema.from_json(json)
# print the JSON string representation of the object
print(ProtectionPolicySecondaryRemoteInputSchema.to_json())

# convert the object into a dict
protection_policy_secondary_remote_input_schema_dict = protection_policy_secondary_remote_input_schema_instance.to_dict()
# create an instance of ProtectionPolicySecondaryRemoteInputSchema from a dict
protection_policy_secondary_remote_input_schema_from_dict = ProtectionPolicySecondaryRemoteInputSchema.from_dict(protection_policy_secondary_remote_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


