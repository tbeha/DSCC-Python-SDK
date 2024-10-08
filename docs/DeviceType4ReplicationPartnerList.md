# DeviceType4ReplicationPartnerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customer ID | [optional] 
**display_name** | **str** | Replication partner display name. | [optional] 
**domain** | **str** | Domain that the resource belongs to. | [optional] 
**dr_state** | **str** | Specifies replication disaster recovery state of a protected volume set.  Possible values: Normal, Failover, Recover, Unknown The disaster recovery state is Unknown for any intermediate state. | [optional] 
**generation** | **int** | generation | [optional] 
**group_id** | **str** | Unique id of replication partner remote group | [optional] 
**group_last_sync_time** | [**DeviceType4SyncTime**](DeviceType4SyncTime.md) |  | [optional] 
**group_name** | **str** | Replication partner remote group name. | [optional] 
**group_object_id** | **int** | Replication partner group ID. | [optional] 
**id** | **str** | Unique Identifier of the replication partner. | [optional] 
**is_protection_policy_configured** | **bool** | Boolean value to indicate if protection policy is properly configured on the volume set. If it is set to false, user needs to either delete the policy or fix the policy configuration. All other operations will be blocked in this scenario. | [optional] 
**is_remote_array_support_replication** | **bool** | Boolean value to indicate if remote array OS version supports replication | [optional] 
**is_source_array_support_replication** | **bool** | Boolean value to indicate if source array OS version supports replication | [optional] 
**mode** | **str** | Replication partner group mode. | [optional] 
**policies** | [**DeviceType4ReplicationPartnerListPolicies**](DeviceType4ReplicationPartnerListPolicies.md) |  | [optional] 
**protection_type** | **str** | Type of protection | [optional] 
**remote_role** | **str** | Specifies remote copy role for a restore point of a protected volume set. In case of synchronous and asynchronous protection polices, restore point is the volume set on the replication partner/target array. Possible values: Primary, Secondary, Primary-Rev, Secondary-Rev, Unknown The role status is Unknown for any intermediate remote copy role for a restore point of a protected volume set. | [optional] 
**remote_usr_cpg** | **str** | Name for which the user space is allocated on the remote target. | [optional] 
**remote_volume_set_name** | **str** | Target volume set name where remote protection is enabled | [optional] 
**replication_traffic** | **str** | Specifies the direction of data replication for the current target. | [optional] 
**resource_uri** | **str** | resourceUri for replication partner list where volume set is remote protected | [optional] 
**role** | **str** | Specifies remote copy role for a protected volume set.  Possible values: Primary, Secondary, Primary-Rev, Secondary-Rev, Unknown The role status is Unknown for any intermediate remote copy role of a protected volume set. | [optional] 
**role_reversed** | **bool** | Remote group role switched due to a fail over. | [optional] 
**snap_frequency_secs** | **int** | Specifies the interval in seconds at which remote group takes coordinated snapshots. This field applies only to Async mode: it is set to -1 otherwise. | [optional] 
**state** | **str** | Status of the Remote group for the replication partner. Can be New, Starting, Started, Restart, Stopped, Backup, Failsafe or Logging. Null if unset. | [optional] 
**sync_period** | **int** | Time period in seconds for automatic resynchronization. The value must be at least five minutes and not more than one year. Defaults to 0. | [optional] 
**system_id** | **str** | Unique ID or serial number of the system. | [optional] 
**system_name** | **str** | Name of the system. | [optional] 
**system_wwn** | **str** | WWN of the system. | [optional] 
**target_name** | **str** | Target to which the volume group is mirrored. This is the same as replication partner. | [optional] 
**type** | **str** | type | [optional] 
**volume_count** | **int** | Number of volumes in the group for a replication partner. | [optional] 

## Example

```python
from dscc.models.device_type4_replication_partner_list import DeviceType4ReplicationPartnerList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ReplicationPartnerList from a JSON string
device_type4_replication_partner_list_instance = DeviceType4ReplicationPartnerList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ReplicationPartnerList.to_json())

# convert the object into a dict
device_type4_replication_partner_list_dict = device_type4_replication_partner_list_instance.to_dict()
# create an instance of DeviceType4ReplicationPartnerList from a dict
device_type4_replication_partner_list_from_dict = DeviceType4ReplicationPartnerList.from_dict(device_type4_replication_partner_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


