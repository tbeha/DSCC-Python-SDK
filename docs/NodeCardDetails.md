# NodeCardDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**fw_version** | **str** | Firmware version | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**node_card_type** | **str** | Type of the node adapter card | [optional] 
**node_device_id** | **int** | ID of the node | [optional] 
**node_id** | **str** | Unique Identifier of the node. | [optional] 
**request_uri** | **str** | requestUri for detailed node card object | [optional] 
**resource_uri** | **str** | resourceUri for detailed node card object | [optional] 
**revision** | **str** | Revision | [optional] 
**safe_to_remove** | **bool** | Indicates if the component is safe to remove | [optional] 
**service_led** | [**LED**](LED.md) |  | [optional] 
**slot** | **int** | Slot of the node adapter card | [optional] 
**system_id** | **str** | systemId/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.node_card_details import NodeCardDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NodeCardDetails from a JSON string
node_card_details_instance = NodeCardDetails.from_json(json)
# print the JSON string representation of the object
print(NodeCardDetails.to_json())

# convert the object into a dict
node_card_details_dict = node_card_details_instance.to_dict()
# create an instance of NodeCardDetails from a dict
node_card_details_from_dict = NodeCardDetails.from_dict(node_card_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


