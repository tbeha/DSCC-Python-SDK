# PrimeraProtectionPolicyPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_recover** | **bool** | If the Remote Copy is stopped as a result of links going down, the Remote Copy group can be automatically restarted after the links come back up. | [optional] 
**auto_synchronize** | **bool** | Auto synchronization ensure that remote copy system automatically recovers and synchronizes all volumes in the group after automatic or manual failover scenarios. In addition, this policy allows failover even when remote copy synchronous groups are started and online | [optional] 
**is_protection_policy_configured** | **bool** | Boolean value to indicate if protection policy is properly configured on the volume set. If it is set to false, user needs to either delete the policy or fix the policy configuration. All other operations will be blocked in this scenario. | [optional] 
**no_automatic_synchronization** | **bool** | Specifies if the no-automatic-synchronization option is enabled in case of Asynchronous/Periodic replication. If this property is true, then no synchronization happens. Not applicable for Synchronous replication. | [optional] 
**non_zero_rto_config** | **str** | Non-Zero RTO configuration. Supported config is Active-Sync. Even the plain synchronous replication is non zero RTO configuration but for this plain sync configuration, no value will be specified in this parameter. | [optional] 
**over_period_alert** | **bool** | This field is valid for 2DC remote replication only, for 3DC remote replication check value of overPeriodAlert within remote and secondaryRemote. If synchronization of an asynchronous periodic Remote Copy group takes longer to complete than its synchronization period, an alert is generated. This property is not valid in case of synchronous policy and will always be false in that case. | [optional] 
**remote** | [**PrimeraRemoteInfo**](PrimeraRemoteInfo.md) | Replication partner details | [optional] 
**rpo_secs** | **int** | Specifies recovery point objective in seconds for Asynchronous periodic protection. This is not applicable for Synchronous replication, and in case of Asynchronous replication, rpoSecs will not contain any value if the no-automatic-synchronization option is enabled. | [optional] 
**secondary_remote** | [**PrimeraRemoteInfo**](PrimeraRemoteInfo.md) | Second replication partner details from Synchronous Long Distance configuration and for 3DC Peer Persistence mode | [optional] 
**zero_rto_config** | **str** | Zero RTO configuration. Supported configs are Active Peer Persistence and Peer Persistence. | [optional] 

## Example

```python
from dscc.models.primera_protection_policy_policy import PrimeraProtectionPolicyPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraProtectionPolicyPolicy from a JSON string
primera_protection_policy_policy_instance = PrimeraProtectionPolicyPolicy.from_json(json)
# print the JSON string representation of the object
print(PrimeraProtectionPolicyPolicy.to_json())

# convert the object into a dict
primera_protection_policy_policy_dict = primera_protection_policy_policy_instance.to_dict()
# create an instance of PrimeraProtectionPolicyPolicy from a dict
primera_protection_policy_policy_from_dict = PrimeraProtectionPolicyPolicy.from_dict(primera_protection_policy_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


