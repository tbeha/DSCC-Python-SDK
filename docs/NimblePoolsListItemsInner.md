# NimblePoolsListItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of pool. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of pool. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. &#x60;Filter, Sort&#x60; | [optional] 
**all_flash** | **bool** | Indicate whether the pool is an all_flash pool. | [optional] 
**array_count** | **int** | Number of arrays in the pool. | [optional] 
**array_list** | [**List[NimbleArrayDetail]**](NimbleArrayDetail.md) | List of arrays in the pool with detailed information. When create/update array list, only arrays&#39; id is required. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**cache_capacity** | **int** | Total usable cache capacity of the pool in bytes. | [optional] 
**capacity** | **int** | Total storage space of the pool in bytes. | [optional] 
**clone_ratio** | **float** | Clone savings for the pool expressed as ratio. Fraction expressed as floating point number. | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**compression_ratio** | **float** | Compression savings for the pool expressed as ratio. Fraction expressed as floating point number. | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int** | Time when this pool was created. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**data_reduction_ratio** | **float** | Space usage savings in the pool expressed as ratio that does not include thin-provisioning savings. Fraction expressed as floating point number. | [optional] 
**dedupe_all_volumes** | **bool** | Indicates if dedupe is enabled by default for new volumes on this pool. | [optional] 
**dedupe_all_volumes_capable** | **bool** | Indicates whether the pool can enable dedupe by default | [optional] 
**dedupe_capable** | **bool** | Indicates whether the pool is capable of hosting deduped volumes. | [optional] 
**dedupe_capacity_bytes** | **int** | The dedupe capacity of a hybrid pool. Does not apply to all-flash pools. | [optional] 
**dedupe_ratio** | **float** | Dedupe savings for the pool expressed as ratio. Fraction expressed as floating point number. | [optional] 
**dedupe_usage_bytes** | **int** | The dedupe usage of a hybrid pool. Does not apply to all-flash pools. | [optional] 
**description** | **str** | Text description of pool. String of up to 255 printable ASCII characters. | [optional] 
**folder_list** | [**List[NimbleFolderSummary]**](NimbleFolderSummary.md) | The list of fully qualified names of folders in the pool. | [optional] 
**free_space** | **int** | Free space of the pool in bytes. | [optional] 
**full_name** | **str** | Fully qualified name of pool. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**generation** | **int** | generation | [optional] 
**is_default** | **bool** | Indicates if this is the default pool. | [optional] 
**last_modified** | **int** | Time when this pool was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**pinnable_cache_capacity** | **int** | Total pinnable cache capacity of the pool in bytes. | [optional] 
**pinned_cache_capacity** | **int** | Total pinned cache capacity of the pool in bytes. | [optional] 
**pinned_vol_list** | [**List[NimblePinnedVolumeInfo]**](NimblePinnedVolumeInfo.md) | The list of pinned volumes in the pool. | [optional] 
**reserve** | **int** | Reserved space of the pool in bytes | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**savings** | **int** | Overall space usage savings in the pool. | [optional] 
**savings_clone** | **int** | Space usage savings in the pool due to cloning of volumes. | [optional] 
**savings_compression** | **int** | Space usage savings in the pool due to compression. | [optional] 
**savings_data_reduction** | **int** | Space usage savings in the pool that does not include thin-provisioning savings. | [optional] 
**savings_dedupe** | **int** | Space usage savings in the pool due to deduplication. | [optional] 
**savings_ratio** | **float** | Overall space usage savings in the pool expressed as ratio. Fraction expressed as floating point number. | [optional] 
**savings_vol_thin_provisioning** | **int** | Space usage savings in the pool due to thin provisioning of volumes. | [optional] 
**search_name** | **str** | Name of pool used for object search. Alphanumeric string, up to 64 characters including hyphen, period, colon. | [optional] 
**snap_count** | **int** | Snapshot count. | [optional] 
**snapcoll_count** | **int** | Snapshot collection count. | [optional] 
**type** | **str** | type | [optional] 
**unassigned_array_list** | [**List[NimbleArrSummary]**](NimbleArrSummary.md) | List of arrays being unassigned from the pool. | [optional] 
**uncompressed_snap_usage_bytes** | **int** | Uncompressed usage of snapshots in the pool | [optional] 
**uncompressed_vol_usage_bytes** | **int** | Uncompressed usage of volumes in the pool | [optional] 
**unused_reserve** | **int** | Unused reserve space of the pool in bytes. | [optional] 
**usage** | **int** | Used space of the pool in bytes. | [optional] 
**usage_valid** | **bool** | Identifier of pool. A 42 digit hexadecimal number. | [optional] 
**vol_count** | **int** | Number of volumes assigned to the pool. | [optional] 
**vol_list** | [**List[NimbleVolumeSummary]**](NimbleVolumeSummary.md) | The list of volumes in the pool. | [optional] 
**vol_thin_provisioning_ratio** | **float** | Thin provisioning savings for volumes in the pool expressed as ratio. Fraction expressed as floating point number. | [optional] 

## Example

```python
from dscc.models.nimble_pools_list_items_inner import NimblePoolsListItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NimblePoolsListItemsInner from a JSON string
nimble_pools_list_items_inner_instance = NimblePoolsListItemsInner.from_json(json)
# print the JSON string representation of the object
print(NimblePoolsListItemsInner.to_json())

# convert the object into a dict
nimble_pools_list_items_inner_dict = nimble_pools_list_items_inner_instance.to_dict()
# create an instance of NimblePoolsListItemsInner from a dict
nimble_pools_list_items_inner_from_dict = NimblePoolsListItemsInner.from_dict(nimble_pools_list_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


