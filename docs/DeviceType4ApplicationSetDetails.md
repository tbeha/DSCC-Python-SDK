# DeviceType4ApplicationSetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_set_business_unit** | **str** | Appset BusinessUnit | [optional] 
**app_set_comments** | **str** | Application set comments | [optional] 
**app_set_exclude_aiqo_s** | **str** | Exclusion from AI QoS | [optional] 
**app_set_id** | **int** | ID | [optional] 
**app_set_importance** | **str** | Importance Level | [optional] 
**app_set_name** | **str** | Application set name | [optional] 
**app_set_qo_s_config** | [**DeviceType4AppSetQoSConfig**](DeviceType4AppSetQoSConfig.md) |  | [optional] 
**app_set_type** | **str** | Type of the application set | [optional] 
**app_set_type_enum** | **str** | Enum value of type of the application set | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**comment** | **str** | Comments if any | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**display_name** | **str** | Display Name | [optional] 
**domain** | **str** | Domain name | [optional] 
**dr_state** | **str** | Specifies replication disaster recovery state of a protected volume set.  Possible values: Normal, Failover, Recover, Unknown The disaster recovery state is Unknown for any intermediate state. | [optional] 
**export_status** | **str** | Export status | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | uid of the applicationset | [optional] 
**initiators** | [**List[DeviceType4ApplicationSetDetailsInitiatorsInner]**](DeviceType4ApplicationSetDetailsInitiatorsInner.md) | Initiator details | [optional] 
**is_failover_allowed** | **bool** | Shows if failover is allowed or not. This field is deprecated. | [optional] 
**is_override_allowed** | **bool** | Shows if Override is allowed or not. This field is deprecated. | [optional] 
**is_primary** | **bool** | States if the Application set is Primary or not | [optional] 
**is_sync_allowed** | **bool** | Shows if sync is allowed or not. This field is deprecated. | [optional] 
**kv_pairs_present** | **bool** | Represents KV pairs present or not | [optional] 
**members** | **List[Optional[str]]** | Volume Names | [optional] 
**name** | **str** | Name of the application set | [optional] 
**non_zero_rto_config** | **str** | Non-Zero RTO configuration. Supported config is Active-Sync | [optional] 
**remote_recovery_point** | [**DeviceType4RecoveryPoint**](DeviceType4RecoveryPoint.md) |  | [optional] 
**replication_partner** | [**List[DeviceType4ApplicationSetDetailsReplicationPartnerInner]**](DeviceType4ApplicationSetDetailsReplicationPartnerInner.md) | Shows the Replication Partner Systems and Replication Partners | [optional] 
**replication_state** | **str** | Shows the replication state of the application set. This is not applicable in case of a 3DC/SLD configuration. | [optional] 
**replication_traffic** | **str** | Shows the direction of flow of data. This is not applicable in case of a 3DC/SLD configuration. | [optional] 
**replication_type** | **str** | Mode of replication. Can be sync or periodic. This is not applicable in case of a 3DC/SLD configuration. | [optional] 
**request_uri** | **str** | RequestUri for applicationsets resources | [optional] 
**role** | **str** | Specifies remote copy role for a protected volume set.  Possible values: Primary, Secondary, Primary-Rev, Secondary-Rev, Unknown The role status is Unknown for any intermediate remote copy role of a protected volume set. | [optional] 
**serial_number** | **str** | Serial number. | [optional] 
**size_mi_b** | **float** | Size in MB of appset | [optional] 
**snap_set_parent_id** | **int** | ParentId of the snapSet | [optional] 
**snap_set_parent_name** | **str** | Parent name of the snapSet | [optional] 
**system_id** | **str** | SystemUid/serialNumber of the array. | [optional] 
**type** | **str** | type | [optional] 
**vv_set_type** | **str** | Type of the volume-set | [optional] 
**zero_rto_config** | **str** | Zero RTO configuration. Supported config is Active Peer Persistence. Classic Peer Persistence is not supported for HPE Alletra Storage MP. | [optional] 

## Example

```python
from dscc.models.device_type4_application_set_details import DeviceType4ApplicationSetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ApplicationSetDetails from a JSON string
device_type4_application_set_details_instance = DeviceType4ApplicationSetDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ApplicationSetDetails.to_json())

# convert the object into a dict
device_type4_application_set_details_dict = device_type4_application_set_details_instance.to_dict()
# create an instance of DeviceType4ApplicationSetDetails from a dict
device_type4_application_set_details_from_dict = DeviceType4ApplicationSetDetails.from_dict(device_type4_application_set_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


