# NimbleSpaceDomainDetailsWithRequestUri


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str** | requestUri for detailed application-summary object | [optional] 
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
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**deduped_volume_count** | **int** | Number of deduplicated volumes belonging to the space domain. | [optional] 
**generation** | **int** | generation | [optional] 
**perf_policy_names** | [**List[NimblePerfPolicySummary]**](NimblePerfPolicySummary.md) | Name of the performance policies associated with the space domain. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 
**sample_rate** | **int** | Sample rate value. | [optional] 
**type** | **str** | type | [optional] 
**volume_count** | **int** | Number of volumes belonging to the space domain. | [optional] 
**volumes** | [**List[NimbleVolumeSummary]**](NimbleVolumeSummary.md) | Volumes belonging to the space domain. | [optional] 

## Example

```python
from dscc.models.nimble_space_domain_details_with_request_uri import NimbleSpaceDomainDetailsWithRequestUri

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleSpaceDomainDetailsWithRequestUri from a JSON string
nimble_space_domain_details_with_request_uri_instance = NimbleSpaceDomainDetailsWithRequestUri.from_json(json)
# print the JSON string representation of the object
print(NimbleSpaceDomainDetailsWithRequestUri.to_json())

# convert the object into a dict
nimble_space_domain_details_with_request_uri_dict = nimble_space_domain_details_with_request_uri_instance.to_dict()
# create an instance of NimbleSpaceDomainDetailsWithRequestUri from a dict
nimble_space_domain_details_with_request_uri_from_dict = NimbleSpaceDomainDetailsWithRequestUri.from_dict(nimble_space_domain_details_with_request_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


