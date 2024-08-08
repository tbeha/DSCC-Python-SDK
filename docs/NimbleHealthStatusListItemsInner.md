# NimbleHealthStatusListItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | Identifier of the array to which this result belongs.&#x60;Filter, Sort&#x60; | [optional] 
**context** | **str** | Context for aggregating health check results. Possible values: &#39;all&#39;, &#39;failover&#39;, &#39;sw_update&#39;.&#x60;Filter, Sort&#x60; | [optional] 
**ctrlr_id** | **str** | Identifier of the controller to which this result belongs.&#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Identifier for the health check. &#x60;Filter&#x60; | [optional] 
**scope** | **str** | Scope at which the health check is to be run.Possible values: &#39;controller&#39;, &#39;array&#39;, &#39;group&#39;.&#x60;Filter, Sort&#x60; | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**NimbleCommonResourceAttributes**](NimbleCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**element_result** | [**NimbleHCFResult**](NimbleHCFResult.md) |  | [optional] 
**generation** | **int** | generation | [optional] 
**on_demand** | **bool** | Flag to indicate running the health checks and then report results. | [optional] 
**resource_uri** | **str** | Link to the object URI | [optional] 

## Example

```python
from dscc.models.nimble_health_status_list_items_inner import NimbleHealthStatusListItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleHealthStatusListItemsInner from a JSON string
nimble_health_status_list_items_inner_instance = NimbleHealthStatusListItemsInner.from_json(json)
# print the JSON string representation of the object
print(NimbleHealthStatusListItemsInner.to_json())

# convert the object into a dict
nimble_health_status_list_items_inner_dict = nimble_health_status_list_items_inner_instance.to_dict()
# create an instance of NimbleHealthStatusListItemsInner from a dict
nimble_health_status_list_items_inner_from_dict = NimbleHealthStatusListItemsInner.from_dict(nimble_health_status_list_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


