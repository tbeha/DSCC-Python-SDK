# NodeBatteryDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**charge_level** | **int** | Battery charge level. | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**discharge_led** | [**LED**](LED.md) |  | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**expiration_date** | [**ExpirationDate**](ExpirationDate.md) |  | [optional] 
**fault_led** | [**LED**](LED.md) |  | [optional] 
**fully_charged** | **bool** | Indicates if battery is fully charged or not | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. | [optional] 
**life** | **int** | Life of the battery | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**max_life** | **int** | Maximum life of the battery | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**node_battery_id** | **int** | Numeric ID of the resource | [optional] 
**power_supply_id** | **int** | Power supply ID for this battery. | [optional] 
**primary_node_id** | **int** | Primary node ID. | [optional] 
**request_uri** | **str** | requestUri for detailed node battery object | [optional] 
**resource_uri** | **str** | resourceUri for detailed node battery object | [optional] 
**safe_to_remove** | **bool** | Indicates if the component is safe to remove | [optional] 
**secondary_node_id** | **int** | Secondary node ID | [optional] 
**service_led** | [**LED**](LED.md) |  | [optional] 
**state** | [**STATE**](STATE.md) |  | [optional] 
**status_led** | [**LED**](LED.md) |  | [optional] 
**system_id** | **str** | systemId/Serial Number  of the array. | [optional] 
**test_in_progress** | **bool** | Indicates if test is in progress or not | [optional] 
**time_to_charge** | **int** | Remaining time to charge | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.node_battery_details import NodeBatteryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NodeBatteryDetails from a JSON string
node_battery_details_instance = NodeBatteryDetails.from_json(json)
# print the JSON string representation of the object
print(NodeBatteryDetails.to_json())

# convert the object into a dict
node_battery_details_dict = node_battery_details_instance.to_dict()
# create an instance of NodeBatteryDetails from a dict
node_battery_details_from_dict = NodeBatteryDetails.from_dict(node_battery_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


