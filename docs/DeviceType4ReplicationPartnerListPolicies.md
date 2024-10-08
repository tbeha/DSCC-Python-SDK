# DeviceType4ReplicationPartnerListPolicies

The policy assigned to the replication partner remote group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_active** | **bool** | Specifies active active policy of the group. | [optional] 
**auto_failover** | **bool** | Automatic failover on a group. | [optional] 
**auto_recover** | **bool** | If the group is stopped as a result of links going down, the group can be automatically restarted after the links come back up. | [optional] 
**auto_synchronize** | **bool** | Specifies auto synchronization of the group. | [optional] 
**multi_target_peer_persistence** | **bool** | Specifies that the group is participating in a Multi-target Peer Persistence configuration. The group must have two targets, one of which must be synchronous.The synchronous group target also requires pathManagement and auto Fail over policy settings. | [optional] 
**over_period_alert** | **bool** | If synchronization of an asynchronous periodic group takes longer to complete than its synchronization period, an alert is generated. | [optional] 
**path_management** | **bool** | Path management on a group. | [optional] 

## Example

```python
from dscc.models.device_type4_replication_partner_list_policies import DeviceType4ReplicationPartnerListPolicies

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ReplicationPartnerListPolicies from a JSON string
device_type4_replication_partner_list_policies_instance = DeviceType4ReplicationPartnerListPolicies.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ReplicationPartnerListPolicies.to_json())

# convert the object into a dict
device_type4_replication_partner_list_policies_dict = device_type4_replication_partner_list_policies_instance.to_dict()
# create an instance of DeviceType4ReplicationPartnerListPolicies from a dict
device_type4_replication_partner_list_policies_from_dict = DeviceType4ReplicationPartnerListPolicies.from_dict(device_type4_replication_partner_list_policies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


