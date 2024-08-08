# NimbleSnapshotDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str** | requestUri for detailed volume snapshot objects | [optional] 
**id** | **str** | Identifier for the snapshot. A 42 digit hexadecimal number. | [optional] 
**is_locked** | **bool** | To verify a snapshot is immutable or not. | [optional] 
**name** | **str** | Name of snapshot. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. | [optional] 
**online** | **bool** | Online state for a snapshot means it could be mounted for data restore. | [optional] 
**pool_name** | **str** | Name of the pool in which the parent volume belongs to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**replication_status** | **str** | Replication status. Possible values: &#39;complete&#39;, &#39;in_progress&#39;, &#39;pending&#39;, &#39;fail&#39;. | [optional] 
**schedule_id** | **str** | Identifier of protection schedule. A 42 digit hexadecimal number. | [optional] 
**schedule_name** | **str** | Name of protection schedule. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**serial_number** | **str** | Identifier for the SCSI protocol. A 32 digit hexadecimal number. | [optional] 
**size** | **int** | Size of volume at time of snapshot (in bytes). | [optional] 
**snap_collection_id** | **str** | Identifier of snapshot collection. A 42 digit hexadecimal number. | [optional] 
**snap_collection_name** | **str** | Name of snapshot collection. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints. | [optional] 
**target_name** | **str** | The iSCSI Qualified Name (IQN) or the Fibre Channel World Wide Node Name (WWNN) of the target snapshot. The iSCSI Qualified Name (IQN) or the Fibre Channel World Wide Node Name (WWNN) of the target. | [optional] 
**writable** | **bool** | Whether snapshot is writable or not. Mandatory and must be set to &#39;true&#39; for VSS application synchronized snapshots. | [optional] 
**access_control_records** | [**List[AccessControlRecord]**](AccessControlRecord.md) | List of access control records that apply to this snapshot. List of access control records associated with a volume or snapshot or protocol endpoint. | [optional] 
**agent_type** | **str** | External management agent type. Possible values: &#39;none&#39;, &#39;smis&#39;, &#39;vvol&#39;, &#39;openstack&#39;, &#39;openstackv2&#39;. | [optional] 
**app_uuid** | **str** | Application identifier of snapshots. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int** | Time when this snapshot was created. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**description** | **str** | Text description of snapshot. String of up to 255 printable ASCII characters. | [optional] 
**expiry_after** | **int** | Number of seconds after which this snapshot is considered expired by snapshot TTL. A value of 0 indicates that snapshot never expires, 1 indicates that snapshot uses group-level configured TTL value and any other value indicates number of seconds. | [optional] 
**expiry_time** | **int** | Unix timestamp indicating that the snapshot is considered expired by Snapshot Time-to-live(TTL). A value of 0 indicates that snapshot never expires. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**generation** | **int** | generation | [optional] 
**is_manually_managed** | **bool** | Is snapshot manually managed, i.e., snapshot is manually or third party created or created by system at the time of volume restore or resize. | [optional] 
**is_mfa_protected** | **bool** | Protected by multi-factor authentication. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**is_replica** | **bool** | Snapshot is a replica from upstream replication partner. | [optional] 
**is_unmanaged** | **bool** | Indicates whether the snapshot is unmanaged. The snapshot will not be deleted automatically unless the unmanaged cleanup feature is enabled. (this argument is deprecated) | [optional] 
**last_modified** | **int** | Time when this snapshot was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**lock_period** | **int** | Number of seconds to keep a snapshot as immutable. | [optional] 
**metadata** | [**List[KeyValue]**](KeyValue.md) | Key-value pairs that augment a snapshot&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. | [optional] 
**new_data_compressed_bytes** | **int** | The bytes of compressed new data. | [optional] 
**new_data_uncompressed_bytes** | **int** | The bytes of uncompressed new data. | [optional] 
**new_data_valid** | **bool** | Indicate the usage information is valid. | [optional] 
**offline_reason** | **str** | Snapshot offline reason - possible entries: one of &#39;user&#39;, &#39;recovery&#39;, &#39;replica&#39;, &#39;over_volume_limit&#39;, &#39;over_snapshot_limit&#39;, &#39;over_volume_reserve&#39;, &#39;nvram_loss_recovery&#39;, &#39;pool_free_space_exhausted&#39; . Possible values: &#39;user&#39;, &#39;recovery&#39;, &#39;replica&#39;, &#39;nvram_loss_recovery&#39;, &#39;serial_number_collision&#39;, &#39;encryption_inactive&#39;, &#39;encryption_key_deleted&#39;, &#39;vvol_unbind&#39;, &#39;cache_unpin_in_progress&#39;, &#39;over_folder_overdraft_limit&#39;, &#39;over_volume_usage_limit&#39;, &#39;pool_free_space_exhausted&#39;, &#39;srep_unconfigured&#39;. | [optional] 
**origin_name** | **str** | Origination group name. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**retention_time** | **int** | Retention time in seconds when the snapshot lock will expire. | [optional] 
**type** | **str** | type | [optional] 
**vol_id** | **str** | Parent volume ID. A 42 digit hexadecimal number. | [optional] 
**vol_name** | **str** | Name of the parent volume in which the snapshot belongs to. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints. | [optional] 
**volume_creator_id** | **str** | Originator id for the snapshot. | [optional] 
**volume_creator_name** | **str** | Originator name for the snapshot. | [optional] 
**vpd_ieee0** | **str** | The first 64 bits of the snapshot&#39;s EUI-64 identifier, encoded as a hexadecimal string. Plain string. | [optional] 
**vpd_ieee1** | **str** | The last 64 bits of the snapshot&#39;s EUI-64 identifier, encoded as a hexadecimal string. Plain string. | [optional] 
**vpd_t10** | **str** | The snapshot&#39;s T10 Vendor ID-based identifier. Plain string. | [optional] 
**snapshot_export_details** | [**NimbleVolumeExportDetails**](NimbleVolumeExportDetails.md) |  | [optional] 

## Example

```python
from dscc.models.nimble_snapshot_details import NimbleSnapshotDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleSnapshotDetails from a JSON string
nimble_snapshot_details_instance = NimbleSnapshotDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleSnapshotDetails.to_json())

# convert the object into a dict
nimble_snapshot_details_dict = nimble_snapshot_details_instance.to_dict()
# create an instance of NimbleSnapshotDetails from a dict
nimble_snapshot_details_from_dict = NimbleSnapshotDetails.from_dict(nimble_snapshot_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


