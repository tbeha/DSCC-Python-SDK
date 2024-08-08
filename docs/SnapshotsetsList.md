# SnapshotsetsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_set_business_unit** | **str** | Appset BusinessUnit | [optional] 
**app_set_comments** | **str** | Application set comments | [optional] 
**app_set_exclude_aiqo_s** | **str** | Exclusion from AI QoS | [optional] 
**app_set_importance** | **str** | Importance Level | [optional] 
**app_set_name** | **str** | Application set name | [optional] 
**app_set_type** | **str** | Type of the snapshotset | [optional] 
**comment** | **str** | Comments if any | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**creation_time** | [**DeviceType4SnapshotsetListSingleCreationTime**](DeviceType4SnapshotsetListSingleCreationTime.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**display_name** | **str** | Display Name | [optional] 
**domain** | **str** | Domain name | [optional] 
**export_status** | **str** | Export status | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | uid of the snapshotset. &#x60;Filter&#x60; | [optional] 
**kv_pairs_present** | **bool** | Represents KV pairs present or not | [optional] 
**members** | **List[Optional[str]]** | Volume Names | [optional] 
**name** | **str** | Name of the snapshotset. &#x60;Filter, Sort&#x60; | [optional] 
**request_uri** | **str** | RequestUri for snapshotsets resources | [optional] 
**serial_number** | **str** | Serial number. | [optional] 
**snap_set_id** | **int** | ID | [optional] 
**snap_set_parent_id** | **int** | ParentId of the snapSet | [optional] 
**snap_set_parent_name** | **str** | Parent name of the snapSet | [optional] 
**system_id** | **str** | SystemUid/serialNumber of the array. | [optional] 
**type** | **str** | type | [optional] 
**vv_set_type** | **str** | Type of the volume-set | [optional] 

## Example

```python
from dscc.models.snapshotsets_list import SnapshotsetsList

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotsetsList from a JSON string
snapshotsets_list_instance = SnapshotsetsList.from_json(json)
# print the JSON string representation of the object
print(SnapshotsetsList.to_json())

# convert the object into a dict
snapshotsets_list_dict = snapshotsets_list_instance.to_dict()
# create an instance of SnapshotsetsList from a dict
snapshotsets_list_from_dict = SnapshotsetsList.from_dict(snapshotsets_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


