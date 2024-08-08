# NimbleSpaceDomainFieldsWithoutSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_category_id** | **str** | Identifier of the application category associated with the space domain. | [optional] 
**app_category_name** | **str** | Name of the application category associated with the space domain. | [optional] 
**block_size** | **int** | Block size in bytes of volumes belonging to the space domain. | [optional] 
**clone_ratio** | **float** | Clone savings for the space domain expressed as ratio. | [optional] 
**compressed_usage_bytes** | **int** | Compressed usage of volumes and snapshots in the space domain. | [optional] 
**compression_ratio** | **float** | Compression savings for the space domain expressed as ratio. | [optional] 
**dedupe_ratio** | **float** | Deduplication savings for the space domain expressed as ratio. | [optional] 
**deduped** | **bool** | Volumes in space domain are deduplicated by default. | [optional] 
**encrypted** | **bool** | Volumes in space domain are encrypted. | [optional] 
**id** | **str** | Identifier of the application summery. | [optional] 
**logical_dedupe_usage** | **int** | Logical space usage of volumes when deduped. | [optional] 
**physical_dedupe_usage** | **int** | Physical space usage of volumes including snapshots when deduped. | [optional] 
**pool_id** | **str** | Identifier associated with the pool in the storage pool table. | [optional] 
**pool_name** | **str** | Name of the pool containing the space domain. | [optional] 
**savings_clone** | **int** | Space usage savings in the space domain due to cloning of volumes. | [optional] 
**savings_compression** | **int** | Space usage savings in the space domain due to compression. | [optional] 
**savings_dedupe** | **int** | Space usage savings in the space domain due to deduplication. | [optional] 
**snap_logical_usage** | **int** | Logical usage of snapshots in the space domain. | [optional] 
**uncompressed_usage_bytes** | **int** | Uncompressed usage of volumes and snapshots in the space domain. | [optional] 
**usage** | **int** | Physical space usage of volumes in the space domain. | [optional] 
**vol_logical_usage** | **int** | Logical usage of volumes in the space domain. | [optional] 
**vol_mapped_usage** | **int** | Mapped usage of volumes in the space domain, useful for computing clone savings. | [optional] 

## Example

```python
from dscc.models.nimble_space_domain_fields_without_sort_key import NimbleSpaceDomainFieldsWithoutSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleSpaceDomainFieldsWithoutSortKey from a JSON string
nimble_space_domain_fields_without_sort_key_instance = NimbleSpaceDomainFieldsWithoutSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleSpaceDomainFieldsWithoutSortKey.to_json())

# convert the object into a dict
nimble_space_domain_fields_without_sort_key_dict = nimble_space_domain_fields_without_sort_key_instance.to_dict()
# create an instance of NimbleSpaceDomainFieldsWithoutSortKey from a dict
nimble_space_domain_fields_without_sort_key_from_dict = NimbleSpaceDomainFieldsWithoutSortKey.from_dict(nimble_space_domain_fields_without_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


