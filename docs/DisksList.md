# DisksList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admit_time** | [**AdmitTime**](AdmitTime.md) |  | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**capacity** | [**FilterDiskCapacity**](FilterDiskCapacity.md) |  | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**consumable_size_mi_b** | **int** | consumable size of disk in MiB | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dev_type** | **str** | Type of the disk. | [optional] 
**disk_id** | **int** | id of the disk | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**fw_status** | **str** | firmware status | [optional] 
**fw_version** | **str** | firmware version | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**life_left_pct** | **float** | Life Left Percentage | [optional] 
**loop_a0** | [**DiskLoop**](DiskLoop.md) |  | [optional] 
**loop_a1** | [**DiskLoop**](DiskLoop.md) |  | [optional] 
**loop_b0** | [**DiskLoop**](DiskLoop.md) |  | [optional] 
**loop_b1** | [**DiskLoop**](DiskLoop.md) |  | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**media_type** | **str** | Media Type of the disk | [optional] 
**mfg_capacity_gb** | **int** | manufacturing capacity of disk in GB | [optional] 
**position_last** | [**DiskPosition**](DiskPosition.md) |  | [optional] 
**position_now** | [**FilterDiskPositionNow**](FilterDiskPositionNow.md) |  | [optional] 
**protocol** | **str** | protocol over the disk | [optional] 
**raw_size_mi_b** | **int** | raw Size of disk in GB | [optional] 
**read_errors** | [**ErrorCount**](ErrorCount.md) |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed disk object | [optional] 
**sed_status** | **str** | SED Status | [optional] 
**speed** | **int** | speed | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**system_id** | **str** | SystemId/SerialNumber of the array. | [optional] 
**temp_max** | **int** | Max Temp of the disk | [optional] 
**temp_min** | **int** | Min Temp of the disk | [optional] 
**temp_now** | **int** | Current Temp of the disk, will be updated at most once in an hour | [optional] 
**type** | **str** | type | [optional] 
**write_errors** | [**ErrorCount**](ErrorCount.md) |  | [optional] 
**wwn** | **str** | unique WWN of the disk. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.disks_list import DisksList

# TODO update the JSON string below
json = "{}"
# create an instance of DisksList from a JSON string
disks_list_instance = DisksList.from_json(json)
# print the JSON string representation of the object
print(DisksList.to_json())

# convert the object into a dict
disks_list_dict = disks_list_instance.to_dict()
# create an instance of DisksList from a dict
disks_list_from_dict = DisksList.from_dict(disks_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


