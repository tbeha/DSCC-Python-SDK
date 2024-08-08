# FleetVolumeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[DeviceType4ReplicationPartnerCommonFieldsAssociatedLinksInner]**](DeviceType4ReplicationPartnerCommonFieldsAssociatedLinksInner.md) | Associated Links | [optional] 
**common_resource_attributes** | [**CommonResourceAttributesfleet**](CommonResourceAttributesfleet.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**health_state** | **str** | Health State of volume.&#x60; | [optional] 
**host_written_capacity_mi_b** | **float** | Host written data size in MiB. | [optional] 
**id** | **str** | UUID string uniquely identifying the storage system object. | [optional] 
**initiators** | [**List[DeviceType4ApplicationSetDetailsInitiatorsInner]**](DeviceType4ApplicationSetDetailsInitiatorsInner.md) | Initiator details. This field is deprecated. | [optional] 
**is_internal** | **bool** | boolean value which specifies if it is a systemVolume or not &#x60;Filter&#x60; | [optional] 
**is_system_volume** | **bool** | boolean value which specifies if it is a systemVolume or not &#x60;Filter&#x60; | [optional] 
**name** | **str** | A user friendly name to identify the storage system volume (resourceName). | [optional] 
**product_family** | **str** | Product Family | [optional] 
**request_uri** | **str** | resourceUri for detailed volume object | [optional] 
**resource_uri** | **str** | resourceUri for detailed volume object | [optional] 
**size_mi_b** | **float** | Size in MiB | [optional] 
**space_warning** | **float** | User alloc space warning | [optional] 
**sub_type** | **str** | subType of the volume | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**thin_savings** | **str** | Thin savings | [optional] 
**type** | **str** | type | [optional] 
**used_capacity_percent** | **float** | Used capacity percentage of volume. &#x60;Filter, Sort&#x60; | [optional] 
**used_size_mi_b** | **float** | Size in MiB | [optional] 
**volume_set_id** | **str** | SystemUid/serialNumber of the volumeSet. | [optional] 
**volume_type** | **str** | VV Type | [optional] 
**wwn** | **str** | Volume wwn. | [optional] 

## Example

```python
from dscc.models.fleet_volume_details import FleetVolumeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FleetVolumeDetails from a JSON string
fleet_volume_details_instance = FleetVolumeDetails.from_json(json)
# print the JSON string representation of the object
print(FleetVolumeDetails.to_json())

# convert the object into a dict
fleet_volume_details_dict = fleet_volume_details_instance.to_dict()
# create an instance of FleetVolumeDetails from a dict
fleet_volume_details_from_dict = FleetVolumeDetails.from_dict(fleet_volume_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


