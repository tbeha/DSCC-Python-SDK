# NodePowerSuppliesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**fanspeed** | **str** | Fan speed of the node power supply | [optional] 
**fanstate** | [**State**](State.md) |  | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**node_power_id** | **int** | Numeric ID of the resource | [optional] 
**primary_node_id** | **int** | Primary node ID. &#x60;Filter, Sort&#x60; | [optional] 
**resource_uri** | **str** | resourceUri for detailed node power object | [optional] 
**safe_to_remove** | **bool** | Indicates if the component is safe to remove | [optional] 
**secondary_node_id** | **int** | Secondary node ID | [optional] 
**service_led** | [**LED**](LED.md) |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.node_power_supplies_list import NodePowerSuppliesList

# TODO update the JSON string below
json = "{}"
# create an instance of NodePowerSuppliesList from a JSON string
node_power_supplies_list_instance = NodePowerSuppliesList.from_json(json)
# print the JSON string representation of the object
print(NodePowerSuppliesList.to_json())

# convert the object into a dict
node_power_supplies_list_dict = node_power_supplies_list_instance.to_dict()
# create an instance of NodePowerSuppliesList from a dict
node_power_supplies_list_from_dict = NodePowerSuppliesList.from_dict(node_power_supplies_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


