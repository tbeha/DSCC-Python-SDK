# DeviceType4ProtectionPolicyRemoteInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** | Remote partner ID | 
**partner_name** | **str** | Remote partner name | 
**replication_partner_snapshot_cpg** | **str** | Replication Partner Snapshot CPG. Applicable only if the target system is Primera or Alletra 9K. Currently, not supported due to OS limitation. This field will be supported in future release. | [optional] 
**replication_partner_user_cpg** | **str** | User CPG in which the target volumes would get created in the replication partner system. | [optional] 
**replication_type** | **str** | Replication type. Synchronous replication/protection policy provides protection from array or site failures with zero RPO. Using this policy, you can also configure zero RTO policy like Active Peer Persistence. Periodic replication (Asynchronous protection policy) provides protection from array or site failure with the user defined RPO. | 

## Example

```python
from dscc.models.device_type4_protection_policy_remote_input_schema import DeviceType4ProtectionPolicyRemoteInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ProtectionPolicyRemoteInputSchema from a JSON string
device_type4_protection_policy_remote_input_schema_instance = DeviceType4ProtectionPolicyRemoteInputSchema.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ProtectionPolicyRemoteInputSchema.to_json())

# convert the object into a dict
device_type4_protection_policy_remote_input_schema_dict = device_type4_protection_policy_remote_input_schema_instance.to_dict()
# create an instance of DeviceType4ProtectionPolicyRemoteInputSchema from a dict
device_type4_protection_policy_remote_input_schema_from_dict = DeviceType4ProtectionPolicyRemoteInputSchema.from_dict(device_type4_protection_policy_remote_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


