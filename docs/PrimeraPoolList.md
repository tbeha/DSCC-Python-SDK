# PrimeraPoolList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | [**CpgAlert**](CpgAlert.md) |  | [optional] 
**allocation_settings** | [**Allocation**](Allocation.md) |  | [optional] 
**ao_config_id** | **float** | Numeric ID of the AO config where the CPG is a member | [optional] 
**associated_links** | [**List[DeviceType4AssociatedLinksInner]**](DeviceType4AssociatedLinksInner.md) | Associated Links Details | [optional] 
**base_size_mi_b** | **int** | Number of LD MiB used in base virtual volumes. &#x60;Filter, Sort&#x60; | [optional] 
**base_size_private_mi_b** | **float** | Number of LD MiB private to individual base virtual volumes, not shared by deduplication | [optional] 
**base_size_raw_mi_b** | **float** | Number of physical (raw) MiB used in base virtual volumes | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**compact_ratio** | **float** | Ratio between the virtual sizes of all volumes in the CPG and the amount of disk space they are currently using. Updated in Cloud Data Store at most once per 30 minutes. | [optional] 
**compress_ratio** | **float** | Ratio between the amount of data written to Dedup Volumes and the amount that is not duplicated. Updated in Cloud Data Store at most once per 30 minutes. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**data_reduce_ratio** | **float** | Ratio between the amount written to all volumes in the CPG and the amount of disk space used after compression and deduplication | [optional] 
**dedup_capable** | **bool** | Indicates whether the CPG supports dedup | [optional] 
**dedup_ratio** | **float** | Ratio between the amount of data written to Dedup Volumes and the amount that is not duplicated. Updated in Cloud Data Store at most once per 30 minutes. | [optional] 
**dedup_version** | [**DeviceType4PoolDetailsDedupVersion**](DeviceType4PoolDetailsDedupVersion.md) |  | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Name of the domain that the CPG belongs to | [optional] 
**free_for_allocation_mi_b** | **float** | Estimated free space for volume allocation (MiB) | [optional] 
**free_size_mi_b** | **float** | Number of LD MiB allocated and available in the CPG. Updated in Cloud Data Store at most once per 30 minutes. &#x60;Filter, Sort&#x60; | [optional] 
**free_size_raw_mi_b** | **float** | Number of physical (raw) MiB allocated and available in the CPG. Updated in Cloud Data Store at most once per 30 minutes. | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**number_of_snap_rc** | **float** | Number of VVs used for Remote copy snapshot CPG usage | [optional] 
**number_of_tdvv** | **float** | Number of TDVVs using the CPG | [optional] 
**number_of_tpvv** | **float** | Number of TPVVs using the CPG | [optional] 
**number_of_user_rc** | **float** | Number of VVs used for Remote copy user CPG usage | [optional] 
**over_prov_ratio** | **float** | Ratio between the virtual sizes of all volumes and the amount of used and free disk spaces. Updated in Cloud Data Store at most once per 30 minutes. | [optional] 
**resource_uri** | **str** | resourceUri for detailed storage-pool object | [optional] 
**sa_grow** | [**CpgGrow**](CpgGrow.md) |  | [optional] 
**sd_grow** | [**CpgGrow**](CpgGrow.md) |  | [optional] 
**shared_size_mi_b** | **float** | Number of LD MiB shared between volumes via deduplication | [optional] 
**snap_size_private_mi_b** | **float** | Number of LD MiB private to individual snapshot virtual volumes, not shared by deduplication. Updated in Cloud Data Store at most once per 30 minutes. | [optional] 
**snap_size_raw_mi_b** | **float** | Number of physical (raw) MiB used in snapshot virtual volumes. Updated in Cloud Data Store at most once per 30 minutes. | [optional] 
**snap_space_admin** | [**SnapSpace**](SnapSpace.md) |  | [optional] 
**snap_space_data** | [**SnapSpace**](SnapSpace.md) |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**storage_pool_id** | **float** | Numeric ID of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**system_id** | **str** | SystemID of the array. &#x60;Filter, Sort&#x60; | [optional] 
**total_reserved_mi_b** | **float** | Total amount of space reserved by CPG  (MiB) | [optional] 
**total_size_mi_b** | **int** | Total logical capacity in the user/snapshot space (MiB). &#x60;Filter, Sort&#x60; | [optional] 
**total_size_raw_mi_b** | **float** | Total physical (raw) MiB in the user/snapshot space | [optional] 
**type** | **str** | type | [optional] 
**user_space** | [**SnapSpace**](SnapSpace.md) |  | [optional] 
**warn_percent** | **float** | Allocation warning percentage | [optional] 

## Example

```python
from dscc.models.primera_pool_list import PrimeraPoolList

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraPoolList from a JSON string
primera_pool_list_instance = PrimeraPoolList.from_json(json)
# print the JSON string representation of the object
print(PrimeraPoolList.to_json())

# convert the object into a dict
primera_pool_list_dict = primera_pool_list_instance.to_dict()
# create an instance of PrimeraPoolList from a dict
primera_pool_list_from_dict = PrimeraPoolList.from_dict(primera_pool_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


