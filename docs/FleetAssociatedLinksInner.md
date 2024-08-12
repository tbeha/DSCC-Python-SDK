# FleetAssociatedLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_uri** | **str** | Resource Uri | [optional] 
**type** | **str** | Resource Type | [optional] 

## Example

```python
from dscc.models.fleet_associated_links_inner import FleetAssociatedLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of FleetAssociatedLinksInner from a JSON string
fleet_associated_links_inner_instance = FleetAssociatedLinksInner.from_json(json)
# print the JSON string representation of the object
print(FleetAssociatedLinksInner.to_json())

# convert the object into a dict
fleet_associated_links_inner_dict = fleet_associated_links_inner_instance.to_dict()
# create an instance of FleetAssociatedLinksInner from a dict
fleet_associated_links_inner_from_dict = FleetAssociatedLinksInner.from_dict(fleet_associated_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


