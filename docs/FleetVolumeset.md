# FleetVolumeset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_type** | **str** | Application name &#x60;Filter&#x60; | [optional] 
**application** | **str** | Application name | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributesfleet**](CommonResourceAttributesfleet.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**health_state** | **str** | health state | [optional] 
**host_written_capacity_mi_b** | **float** | Host written capacity in MiB | [optional] 
**id** | **str** | id of the volume set &#x60;Filter&#x60; | [optional] 
**intrinsic_resource** | **str** | Intrinsic resource type | [optional] 
**iops** | **float** | IOPS | [optional] 
**is_internal** | **bool** | Is an internal resource | [optional] 
**latency** | **float** | Latency | [optional] 
**location** | **str** | location | [optional] 
**members** | **List[str]** | Members of the volume set. This field is deprecated. | [optional] 
**name** | **str** | name of volume-set &#x60;Filter, Sort&#x60; | [optional] 
**product_family** | **str** | Product Family | [optional] 
**provisioned_size_mi_b** | **float** | Provisioned size in MiB | [optional] 
**resource_uri** | **str** | resourceUri for detailed volume object | [optional] 
**size_mi_b** | **float** | Size in MiB | [optional] 
**space_warning** | **float** | Space warning set for the resource | [optional] 
**sub_type** | **str** | subType | [optional] 
**system_id** | **str** | system ID. &#x60;Filter, Sort&#x60; | [optional] 
**thin_savings** | **str** | ThinSavings | [optional] 
**through_put** | **float** | ThroughPut for the resource | [optional] 
**total_reserved_mi_b** | **float** | Total reserved MiB for the resource | [optional] 
**type** | **str** | type | [optional] 
**used_capacity_percent** | **float** | Used capacity percentage | [optional] 
**used_size_mi_b** | **float** | Used size in MiB | [optional] 
**volume_set_id** | **str** | UID of the volume set Id | [optional] 
**volume_type** | **str** | Type of volume | [optional] 
**wwn** | **str** | wwn of the volume | [optional] 

## Example

```python
from dscc.models.fleet_volumeset import FleetVolumeset

# TODO update the JSON string below
json = "{}"
# create an instance of FleetVolumeset from a JSON string
fleet_volumeset_instance = FleetVolumeset.from_json(json)
# print the JSON string representation of the object
print(FleetVolumeset.to_json())

# convert the object into a dict
fleet_volumeset_dict = fleet_volumeset_instance.to_dict()
# create an instance of FleetVolumeset from a dict
fleet_volumeset_from_dict = FleetVolumeset.from_dict(fleet_volumeset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


