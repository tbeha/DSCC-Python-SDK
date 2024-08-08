# FleetSystemVolumeset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_type** | **str** | Application name &#x60;Filter&#x60; | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributesfleet**](CommonResourceAttributesfleet.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | id of the volume set &#x60;Filter&#x60; | [optional] 
**name** | **str** | name of volume-set &#x60;Filter, Sort&#x60; | [optional] 
**product_family** | **str** | Product Family | [optional] 
**request_uri** | **str** | RequestUri for applicationsets resources | [optional] 
**resource_uri** | **str** | resourceUri for detailed volume object | [optional] 
**system_id** | **str** | system ID. &#x60;Filter, Sort&#x60; | [optional] 
**type** | **str** | type | [optional] 
**volumes_count** | **int** | The number of volumes in an application | [optional] 

## Example

```python
from dscc.models.fleet_system_volumeset import FleetSystemVolumeset

# TODO update the JSON string below
json = "{}"
# create an instance of FleetSystemVolumeset from a JSON string
fleet_system_volumeset_instance = FleetSystemVolumeset.from_json(json)
# print the JSON string representation of the object
print(FleetSystemVolumeset.to_json())

# convert the object into a dict
fleet_system_volumeset_dict = fleet_system_volumeset_instance.to_dict()
# create an instance of FleetSystemVolumeset from a dict
fleet_system_volumeset_from_dict = FleetSystemVolumeset.from_dict(fleet_system_volumeset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


