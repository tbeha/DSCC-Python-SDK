# ProtectionPolicyRemoteInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** | Remote partner ID | 
**partner_name** | **str** | Remote partner name | 
**replication_partner_snapshot_cpg** | **str** | Replication Partner Snapshot CPG. Applicable only if the target system is Primera or Alletra 9K. | [optional] 
**replication_partner_user_cpg** | **str** | Replication Partner User CPG | [optional] 
**replication_type** | **str** | Replication type. Synchronous replication/protection policy provides protection from array or site failures with zero RPO. Using this policy, you can also configure zero RTO policy like Active Peer Persistence. Periodic replication (Asynchronous protection policy) provides protection from array or site failure with the user defined RPO. | 

## Example

```python
from dscc.models.protection_policy_remote_input_schema import ProtectionPolicyRemoteInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionPolicyRemoteInputSchema from a JSON string
protection_policy_remote_input_schema_instance = ProtectionPolicyRemoteInputSchema.from_json(json)
# print the JSON string representation of the object
print(ProtectionPolicyRemoteInputSchema.to_json())

# convert the object into a dict
protection_policy_remote_input_schema_dict = protection_policy_remote_input_schema_instance.to_dict()
# create an instance of ProtectionPolicyRemoteInputSchema from a dict
protection_policy_remote_input_schema_from_dict = ProtectionPolicyRemoteInputSchema.from_dict(protection_policy_remote_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


