# FleetVolumeSetDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_type** | **str** | Application name &#x60;Filter&#x60; | [optional] 
**application** | **str** | Application name | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributesfleet**](CommonResourceAttributesfleet.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | id of the volume set &#x60;Filter&#x60; | [optional] 
**name** | **str** | name of volume-set &#x60;Filter, Sort&#x60; | [optional] 
**product_family** | **str** | Product Family | [optional] 
**resource_uri** | **str** | resourceUri for detailed volume object | [optional] 
**system_id** | **str** | system ID. &#x60;Filter, Sort&#x60; | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.fleet_volume_set_details import FleetVolumeSetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FleetVolumeSetDetails from a JSON string
fleet_volume_set_details_instance = FleetVolumeSetDetails.from_json(json)
# print the JSON string representation of the object
print(FleetVolumeSetDetails.to_json())

# convert the object into a dict
fleet_volume_set_details_dict = fleet_volume_set_details_instance.to_dict()
# create an instance of FleetVolumeSetDetails from a dict
fleet_volume_set_details_from_dict = FleetVolumeSetDetails.from_dict(fleet_volume_set_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


