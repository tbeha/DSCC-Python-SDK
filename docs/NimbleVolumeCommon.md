# NimbleVolumeCommon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_control_records** | [**List[AccessControlRecord]**](AccessControlRecord.md) | List of access control records that apply to this volume. List of access control records associated with a volume or snapshot or protocol endpoint. | [optional] 
**agent_type** | **str** | External management agent type. Possible values: &#39;none&#39;, &#39;smis&#39;, &#39;vvol&#39;, &#39;openstack&#39;, &#39;openstackv2&#39;. | [optional] 
**app_category** | **str** | Application category that the volume belongs to. Plain string. | [optional] 
**app_uuid** | **str** | Application identifier of volume. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**block_size** | **int** | Size in bytes of blocks in the volume. | [optional] 
**cache_needed_for_pin** | **int** | The amount of flash needed to pin the volume. | [optional] 
**cache_pinned** | **bool** | If set to true, all the contents of this volume are kept in flash cache. This provides for consistent performance guarantees for all types of workloads. The amount of flash needed to pin the volume is equal to the limit for the volume. | [optional] 
**cache_policy** | **str** | Cache policy applied to the volume. Possible values: &#39;disabled&#39;, &#39;normal&#39;, &#39;aggressive&#39;, &#39;no_write&#39;, &#39;aggressive_read_no_write&#39;. | [optional] 
**caching_enabled** | **bool** | Indicate caching the volume is enabled. | [optional] 
**cksum_last_verified** | **int** | Last checksum verification time. | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**content_repl_errors_found** | **bool** | Indicates whether the last content based replication had errors. | [optional] 
**creation_time** | **int** | Time when this volume was created. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dedupe_enabled** | **bool** | Indicate whether dedupe is enabled. | [optional] 
**description** | **str** | Text description of volume. String of up to 255 printable ASCII characters. | [optional] 
**encryption_cipher** | **str** | The encryption cipher of the volume. Possible values: &#39;none&#39;, &#39;aes_256_xts&#39;. | [optional] 
**force** | **bool** | Forcibly offline, reduce size or change read-only status a volume. | [optional] 
**full_name** | **str** | Fully qualified name of volume. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. | [optional] 
**generation** | **int** | generation | [optional] 
**has_locked_snapshots** | **bool** | To verify a volume has an immutable snapshot or not. | [optional] 
**inherit_acl** | **bool** | In a volume clone operation, if both the parent and the clone have no external management agent (their agent_type property is \&quot;none\&quot;), then inherit_acl controls whether the clone will inherit a copy of the parent&#39;s access control list. If either the parent or the clone have an external management agent, then the clone will not inherit the parent&#39;s access control list. | [optional] 
**is_mfa_protected** | **bool** | Protected by multi-factor authentication. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**iscsi_target_scope** | **str** | This indicates whether volume is exported under iSCSI Group Target or iSCSI Volume Target. This attribute is only meaningful to iSCSI system. On FC system, all volumes are exported under the FC Group Target. In create operation, the volume&#39;s target type will be set by this attribute. If not specified, it will be set as the group-setting. In clone operation, the clone&#39;s target type will inherit from the parent&#39; setting. Possible values: &#39;volume&#39;, &#39;group&#39;. | [optional] 
**last_content_snap_br_cg_uid** | **int** | The branch cg uid of the content based snapshot that was last replicated. | [optional] 
**last_content_snap_br_gid** | **int** | The branch gid of the content based snapshot that was last replicated. | [optional] 
**last_content_snap_id** | **int** | The ID of the content based snapshot that was last replicated. | [optional] 
**last_modified** | **int** | Time when this volume was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**last_snap** | [**SnapSummary**](SnapSummary.md) |  | [optional] 
**limit** | **int** | Limit for the volume as a percentage of volume size. Percentage as integer from 0 to 100. | [optional] 
**limit_iops** | **int** | IOPS limit for this volume. If limit_iops is not specified when a volume is created, or if limit_iops is set to -1, then the volume has no IOPS limit. If limit_iops is not specified while creating a clone, IOPS limit of parent volume will be used as limit. IOPS limit should be in range [256, 4294967294] or -1 for unlimited. If both limit_iops and limit_mbps are specified, limit_mbps must not be hit before limit_iops. In other words, IOPS and MBPS limits should honor limit_iops _ampersand_amp;lt;&#x3D; ((limit_mbps MB/s * 2^20 B/MB) / block_size B). | [optional] 
**limit_mbps** | **int** | Throughput limit for this volume in MB/s. If limit_mbps is not specified when a volume is created, or if limit_mbps is set to -1, then the volume has no MBPS limit. MBPS limit should be in range [1, 4294967294] or -1 for unlimited. If both limit_iops and limit_mbps are specified, limit_mbps must not be hit before limit_iops. In other words, IOPS and MBPS limits should honor limit_iops _ampersand_amp;lt;&#x3D; ((limit_mbps MB/s * 2^20 B/MB) / block_size B). | [optional] 
**metadata** | [**List[KeyValue]**](KeyValue.md) | Key-value pairs that augment a volume&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. | [optional] 
**move_aborting** | **bool** | This indicates whether the move of the volume is aborting or not. | [optional] 
**move_bytes_migrated** | **int** | The bytes of volume which have been moved. | [optional] 
**move_bytes_remaining** | **int** | The bytes of volume which have not been moved. | [optional] 
**move_est_compl_time** | **int** | The estimated time of completion of a move. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**move_start_time** | **int** | The Start time when this volume was moved. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**multi_initiator** | **bool** | This indicates whether volume and its snapshots are multi-initiator accessible. This attribute applies only to volumes and snapshots available to iSCSI initiators.Online state of volume, available for host initiators to establish connections. | [optional] 
**needs_content_repl** | **bool** | Indicates whether the volume needs content based replication. | [optional] 
**num_snaps** | **int** | Number of live, non-hidden snapshots for this volume. | [optional] 
**offline_reason** | **str** | Volume offline reason. Possible values: &#39;user&#39;, &#39;recovery&#39;, &#39;replica&#39;, &#39;over_volume_limit&#39;, &#39;over_snapshot_limit&#39;, &#39;over_volume_reserve&#39;, &#39;over_snapshot_reserve&#39;, &#39;nvram_loss_recovery&#39;, &#39;serial_number_collision&#39;, &#39;encryption_inactive&#39;, &#39;encryption_key_deleted&#39;, &#39;vvol_unbind&#39;, &#39;cache_unpin_in_progress&#39;. | [optional] 
**online_snaps** | [**List[SnapshotFromVolume]**](SnapshotFromVolume.md) | The list of online snapshots of this volume. Snapshot list as presented in volumes object set. | [optional] 
**perfpolicy_creator_id** | **str** | Originator id for the associated performance policy. | [optional] 
**perfpolicy_creator_name** | **str** | Originator name for the associated performance policy. | [optional] 
**pinned_cache_size** | **int** | The amount of flash pinned on the volume. | [optional] 
**pre_filter** | **str** | Pre-filtering criteria. Plain string. | [optional] 
**previously_deduped** | **bool** | Indicate whether dedupe has ever been enabled on this volume. | [optional] 
**projected_num_snaps** | **int** | Depricated. Projected number of snapshots (including schedued and manual) for this volume. | [optional] 
**protection_type** | **str** | Specifies if volume is protected with schedules. If protected, indicate whether replication is setup. Volume Collection or volume is protected locally or remotely or unprotected. Possible values: &#39;local&#39;, &#39;remote&#39; or &#39;unprotected&#39;. | [optional] 
**reserve** | **int** | Amount of space to reserve for this volume as a percentage of volume size. Percentage as integer either 0 or 100. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**search_name** | **str** | Name of volume used for object search. Alphanumeric string, up to 64 characters including hyphen, period, colon. | [optional] 
**snap_reserve** | **int** | Amount of space to reserve for snapshots of this volume as a percentage of volume size. | [optional] 
**snap_usage_compressed_bytes** | **int** | Sum of compressed backup data in bytes stored in snapshots of this volume. | [optional] 
**snap_usage_populated_bytes** | **int** | Sum of backup data in bytes stored in snapshots of this volume without accounting for the sharing of data between snapshots. | [optional] 
**snap_usage_uncompressed_bytes** | **int** | Sum of uncompressed unique backup data in bytes stored in snapshots of this volume. | [optional] 
**snap_warn_level** | **int** | Threshold for available space as a percentage of volume size below which an alert is raised. | [optional] 
**space_usage_level** | **str** | Indicates space usage level based on warning level. Possible values: &#39;normal&#39;, &#39;warning&#39;, &#39;critical&#39;. | [optional] 
**srep_last_sync** | **int** | Time when synchronously replicated volume was last synchronized. | [optional] 
**srep_resync_percent** | **int** | Percentage of resync progress for synchronously replicated volume. | [optional] 
**thinly_provisioned** | **bool** | Allow volume to be advertised as thinly provisioned to initiators supporting thin provisioning. For such volumes, soft limit notification is set to initiators when the volume space usage crosses its volume_warn_level. Default is yes. This change takes effect only for new connections to the volume. Initiators must disconnect and reconnect for the new setting to be take effect at the initiator level consistently. | [optional] 
**total_usage_bytes** | **int** | Sum of compressed data and compressed backup data in bytes of this volume. | [optional] 
**type** | **str** | type | [optional] 
**upstream_cache_pinned** | **bool** | This indicates whether the upstream volume is cache pinned or not. | [optional] 
**usage_valid** | **bool** | This indicates whether usage information of volume and snapshots are valid or not. | [optional] 
**vol_state** | **str** | Status of the volume.  Possible values: &#39;online&#39;, &#39;offline&#39;, &#39;non_writable&#39;, &#39;read_only&#39;, &#39;login_only&#39;. | [optional] 
**vol_usage_compressed_bytes** | **int** | Compressed data in bytes for this volume. | [optional] 
**vol_usage_mapped_bytes** | **int** | Mapped data in bytes for this volume. | [optional] 
**vol_usage_uncompressed_bytes** | **int** | Uncompressed data in bytes for this volume. | [optional] 
**volcoll_creator_id** | **str** | Originator id for the associated volume collection. | [optional] 
**volcoll_creator_name** | **str** | Originator name for the associated volume collection. | [optional] 
**volume_creator_id** | **str** | Originator id for the volume. | [optional] 
**volume_creator_name** | **str** | Originator name for the volume. | [optional] 
**vpd_ieee0** | **str** | The first 64 bits of the volume&#39;s EUI-64 identifier, encoded as a hexadecimal string. Plain string. | [optional] 
**vpd_ieee1** | **str** | The last 64 bits of the volume&#39;s EUI-64 identifier, encoded as a hexadecimal string. Plain string. | [optional] 
**vpd_t10** | **str** | The volume&#39;s T10 Vendor ID-based identifier. Plain string. | [optional] 
**warn_level** | **int** | Threshold for available space as a percentage of volume size below which an alert is raised. If this option is not specified, array default volume warn level setting is used to decide the warning level for this volume. | [optional] 

## Example

```python
from dscc.models.nimble_volume_common import NimbleVolumeCommon

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleVolumeCommon from a JSON string
nimble_volume_common_instance = NimbleVolumeCommon.from_json(json)
# print the JSON string representation of the object
print(NimbleVolumeCommon.to_json())

# convert the object into a dict
nimble_volume_common_dict = nimble_volume_common_instance.to_dict()
# create an instance of NimbleVolumeCommon from a dict
nimble_volume_common_from_dict = NimbleVolumeCommon.from_dict(nimble_volume_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


