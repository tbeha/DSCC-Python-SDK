# NodeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int** | Numeric ID of the resource. | [optional] 
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**bios_version** | **str** | Bios version | [optional] 
**cache_available_pct** | **int** | Percentage of the cache available | [optional] 
**cache_enabled** | **int** | Percentage of the cache enabled on the node | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**control_memory_mi_b** | **int** | Total control memory in the node in MiB | [optional] 
**customer_id** | **str** | customerId | [optional] 
**data_memory_mi_b** | **int** | Total data memory in the node in MiB | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. | [optional] 
**in_cluster** | **bool** | Indicates if this node is part of the cluster. | [optional] 
**kernel_version** | **str** | Kernel version | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**master** | **bool** | Indicates if this is the master node. | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**online** | **bool** | Indicates if this node is online | [optional] 
**request_uri** | **str** | requestUri for detailed node object | [optional] 
**resource_uri** | **str** | resourceUri for detailed node object | [optional] 
**safe_to_remove** | **bool** | Indicates if the component is safe to remove | [optional] 
**service_led** | **str** | LED state. | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**state_description** | **str** | State of the resource | [optional] 
**system_id** | **str** | SystemId/Serial Number  of the array. | [optional] 
**system_led** | [**LED**](LED.md) |  | [optional] 
**type** | **str** | type | [optional] 
**uptime** | [**Nodeuptime**](Nodeuptime.md) |  | [optional] 

## Example

```python
from dscc.models.node_details import NodeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NodeDetails from a JSON string
node_details_instance = NodeDetails.from_json(json)
# print the JSON string representation of the object
print(NodeDetails.to_json())

# convert the object into a dict
node_details_dict = node_details_instance.to_dict()
# create an instance of NodeDetails from a dict
node_details_from_dict = NodeDetails.from_dict(node_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


