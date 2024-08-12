# NimbleHealthStatusWithDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**element_result** | [**NimbleHCFResult**](NimbleHCFResult.md) |  | [optional] 
**generation** | **int** | generation | [optional] 
**on_demand** | **bool** | Flag to indicate running the health checks and then report results. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 

## Example

```python
from dscc.models.nimble_health_status_with_details import NimbleHealthStatusWithDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleHealthStatusWithDetails from a JSON string
nimble_health_status_with_details_instance = NimbleHealthStatusWithDetails.from_json(json)
# print the JSON string representation of the object
print(NimbleHealthStatusWithDetails.to_json())

# convert the object into a dict
nimble_health_status_with_details_dict = nimble_health_status_with_details_instance.to_dict()
# create an instance of NimbleHealthStatusWithDetails from a dict
nimble_health_status_with_details_from_dict = NimbleHealthStatusWithDetails.from_dict(nimble_health_status_with_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


