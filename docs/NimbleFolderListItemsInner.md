# NimbleFolderListItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the folder. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of the folder. &#x60;Filter, Sort&#x60; | [optional] 
**pool_id** | **str** | ID of the pool where the folder resides.&#x60;Filter, Sort&#x60; | [optional] 
**pool_name** | **str** | Name of the pool where the folder resides.&#x60;Filter, Sort&#x60; | [optional] 
**access_protocol** | **str** | Access protocol of the folder. This attribute is used by the VASA Provider to determine the access protocol of the bind request. If not specified in the creation request, it will be the access protocol supported by the group. If the group supports multiple protocols, the default will be Fibre Channel. This field is meaningful only to VVol folder. Possible values: &#39;iscsi&#39;, &#39;fc&#39;. | [optional] 
**agent_type** | **str** | External management agent type. Possible values: &#39;none&#39;, &#39;smis&#39;, &#39;vvol&#39;, &#39;openstack&#39;. | [optional] 
**app_uuid** | **str** | Application identifier of the folder. | [optional] 
**appserver_id** | **str** | Identifier of the application server associated with the folder. | [optional] 
**appserver_name** | **str** | Name of the application server associated with the folder. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**capacity_bytes** | **int** | Capacity of the folder in bytes. If the folder&#39;s size has a usage limit, capacity_bytes will be the folder&#39;s usage limit. If the folder&#39;s size does not have a usage limit, capacity_bytes will be the pool&#39;s capacity. This field is meaningful only when the usage_valid attribute is true. | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**compressed_snap_usage_bytes** | **int** | Compressed usage of snapshots in the folder. This field is meaningful only when the usage_valid attribute is true. | [optional] 
**compressed_vol_usage_bytes** | **int** | Compressed usage of volumes in the folder. This field is meaningful only when the usage_valid attribute is true. | [optional] 
**compression_ratio** | **float** | Compression savings for the folder expressed as ratio. This field is meaningful only when the usage_valid attribute is true. | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int** | Time when this folder was created. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**description** | **str** | Text description of folder. | [optional] 
**folset_id** | **str** | Identifier of the folder set associated with the folder. Only VVol folder can be associated with the folder set. The folder and the containing folder set must be associated with the same application server. | [optional] 
**folset_name** | **str** | Name of the folder set associated with the folder. Only VVol folder can be associated with the folder set. The folder and the containing folder set must be associated with the same application server. | [optional] 
**fqn** | **str** | Fully qualified name of folder in the pool. | [optional] 
**free_space_bytes** | **int** | Free space in the folder in bytes. If the folder has a usage limit, free_space_bytes will be the folder&#39;s free space (the folder&#39;s usage limit minus the folder&#39;s space usage). If the folder does not have a usage limit, free_space_bytes will be the pool&#39;s free space. This field is meaningful only when the usage_valid attribute is true. | [optional] 
**full_name** | **str** | Fully qualified name of folder in the group. | [optional] 
**generation** | **int** | generation | [optional] 
**inherited_vol_perfpol_id** | **str** | Identifier of the default performance policy for a newly created volume. | [optional] 
**inherited_vol_perfpol_name** | **str** | Name of the default performance policy for a newly created volume. | [optional] 
**last_modified** | **int** | Identifier of the default performance policy for a newly created volume. | [optional] 
**limit_bytes** | **int** | Folder limit size in bytes. By default, a folder (except SMIS and VVol types) does not have a limit. If limit_bytes is not specified when a folder is created, or if limit_bytes is set to the largest possible 64-bit signed integer (9223372036854775807), then the folder has no limit. Otherwise, a limit smaller than the capacity of the pool can be set. On output, if the folder has a limit, the limit_bytes_specified attribute will be true and limit_bytes will be the limit. If the folder does not have a limit, the limit_bytes_specified attribute will be false and limit_bytes will be interpreted based on the value of the usage_valid attribute. If the usage_valid attribute is true, limits_byte will be the capacity of the pool. Otherwise, limits_bytes is not meaningful and can be null. SMIS and VVol folders require a size limit. This attribute is superseded by limit_size_bytes. | [optional] 
**limit_bytes_specified** | **bool** | Indicates whether the folder has a limit. | [optional] 
**limit_iops** | **int** | IOPS limit for this folder. If limit_iops is not specified when a folder is created, or if limit_iops is set to -1, then the folder has no IOPS limit. IOPS limit should be in range [256, 4294967294] or -1 for unlimited. | [optional] 
**limit_mbps** | **int** | Throughput limit for this folder in MB/s. If limit_mbps is not specified when a folder is created, or if limit_mbps is set to -1, then the folder has no throughput limit. MBPS limit should be in range [1, 4294967294] or -1 for unlimited. | [optional] 
**limit_size_bytes** | **int** | Folder size limit in bytes. If limit_size_bytes is not specified when a folder is created, or if limit_size_bytes is set to -1, then the folder has no limit. Otherwise, a limit smaller than the capacity of the pool can be set. Folders with an agent_type of &#39;smis&#39; or &#39;vvol&#39; must have a size limit. | [optional] 
**num_snapcolls** | **int** | Number of snapshot collections inside the folder. This attribute is deprecated and has no meaningful value. | [optional] 
**num_snaps** | **int** | Number of snapshots inside the folder. This attribute is deprecated and has no meaningful value. | [optional] 
**overdraft_limit_pct** | **int** | Amount of space to consider as overdraft range for this folder as a percentage of folder used limit. Valid values are from 0% - 200%. This is the limit above the folder usage limit beyond which enforcement action(volume offline/non-writable) is issued. | [optional] 
**provisioned_bytes** | **int** | Sum of provisioned size of volumes in the folder. | [optional] 
**provisioned_limit_size_bytes** | **int** | Limit on the provisioned size of volumes in a folder. If provisioned_limit_size_bytes is not specified when a folder is created, or if provisioned_limit_size_bytes is set to -1, then the folder has no provisioned size limit. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**search_name** | **str** | Name of folder used for object search. | [optional] 
**snap_compression_ratio** | **float** | Identifier of the default performance policy for a newly created volume. | [optional] 
**tenant_id** | **str** | Tenant ID of the folder. This is used to determine what tenant context the folder belongs to. | [optional] 
**type** | **str** | type | [optional] 
**uncompressed_snap_usage_bytes** | **int** | Uncompressed usage of snapshots in the folder. This field is meaningful only when the usage_valid attribute is true. | [optional] 
**uncompressed_vol_usage_bytes** | **int** | Uncompressed usage of volumes in the folder. This field is meaningful only when the usage_valid attribute is true. | [optional] 
**unused_reserve_bytes** | **int** | Unused reserve of volumes in the folder in bytes. This field is meaningful only when the usage_valid attribute is true. | [optional] 
**unused_snap_reserve_bytes** | **int** | Unused reserve of snapshots of volumes in the folder in bytes. This field is meaningful only when the usage_valid attribute is true. | [optional] 
**usage_bytes** | **int** | Sum of mapped usage and snapshot uncompressed usage of volumes in the folder. | [optional] 
**usage_valid** | **bool** | Indicate whether the space usage attributes of folder are valid. | [optional] 
**vol_compression_ratio** | **float** | Compression ratio of volumes in the folder. This field is meaningful only when the usage_valid attribute is true. | [optional] 
**volume_list** | [**List[NimbleVolumeSummary]**](NimbleVolumeSummary.md) | List of volumes contained by the folder. | [optional] 
**volume_mapped_bytes** | **int** | Sum of mapped usage of volumes in the folder. | [optional] 

## Example

```python
from dscc.models.nimble_folder_list_items_inner import NimbleFolderListItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFolderListItemsInner from a JSON string
nimble_folder_list_items_inner_instance = NimbleFolderListItemsInner.from_json(json)
# print the JSON string representation of the object
print(NimbleFolderListItemsInner.to_json())

# convert the object into a dict
nimble_folder_list_items_inner_dict = nimble_folder_list_items_inner_instance.to_dict()
# create an instance of NimbleFolderListItemsInner from a dict
nimble_folder_list_items_inner_from_dict = NimbleFolderListItemsInner.from_dict(nimble_folder_list_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


