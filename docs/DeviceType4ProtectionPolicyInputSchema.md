# DeviceType4ProtectionPolicyInputSchema

Protection policy details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_recover** | **bool** | Specifies that if the protected volume set is stopped as a result of the Remote Copy links going down, the protected volume set is restarted automatically after the links come back up.  If this policy is enabled for a volume set while the volume set is stopped after link failures, it will only be started when the links come up for the failed target.  If the links are already up at the time the policy is set, then the protected volume set will not be restarted at that time. | [optional] 
**auto_synchronize** | **object** | This property ensures that the Remote Copy system automatically recovers and synchronizes all volumes in the protected volume set after a system failover, for either automatic or manual failover scenarios.  Synchronization occurs after system recovery completes and the Remote Copy links recover. This policy also allows the failover command to be used when synchronous volume sets are started and are online.  It is no longer necessary to stop the synchronous volume sets before initiating a failover command to the secondary system. | [optional] 
**no_automatic_synchronization** | **bool** | Enabling this option results in no synchronization happening between the source and target application sets. This is applicable only in case of periodic replication, and is disabled by default. | [optional] 
**over_period_alert** | **bool** | If synchronization of an asynchronous periodic protection takes longer to complete than its synchronization period, an alert is generated. This property is not valid and hence cannot be enabled in case of synchronous replication. | [optional] 
**remote** | [**DeviceType4ProtectionPolicyRemoteInputSchema**](DeviceType4ProtectionPolicyRemoteInputSchema.md) | Replication partner details for remote protection | 
**rpo_secs** | **int** | Specifies recovery point objective in seconds for asynchronous periodic protection. Range: 30 - 63072000, and should be an even number. For Synchronous replication, the value defaults to zero even if it is specified. For Asynchronous replication, if rpoSecs is not specified then it would be considered under the no-automatic-synchronization option, and no synchronization happens. | [optional] 
**secondary_remote** | [**DeviceType4ProtectionPolicySecondaryRemoteInputSchema**](DeviceType4ProtectionPolicySecondaryRemoteInputSchema.md) | Replication partner details for Async partner in Synchronous Long Distance mode and for 3DC Peer Persistence mode | [optional] 
**zero_rto_config** | **str** | Zero RTO configuration to be used. Supported config is Active Peer Persistence. Classic Peer Persistence is not supported by HPE Alletra Storage MP. If this is not specified, the configuration will be Plain Synchronous Configuration.  | [optional] 

## Example

```python
from dscc.models.device_type4_protection_policy_input_schema import DeviceType4ProtectionPolicyInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ProtectionPolicyInputSchema from a JSON string
device_type4_protection_policy_input_schema_instance = DeviceType4ProtectionPolicyInputSchema.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ProtectionPolicyInputSchema.to_json())

# convert the object into a dict
device_type4_protection_policy_input_schema_dict = device_type4_protection_policy_input_schema_instance.to_dict()
# create an instance of DeviceType4ProtectionPolicyInputSchema from a dict
device_type4_protection_policy_input_schema_from_dict = DeviceType4ProtectionPolicyInputSchema.from_dict(device_type4_protection_policy_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


