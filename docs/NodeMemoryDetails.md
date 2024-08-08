# NodeMemoryDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**cache_type** | **str** | Type of the cache memory is used for | [optional] 
**cas_latency** | **str** | CAS latency | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | UUID string uniquely identifying the node object. | [optional] 
**jedec_id** | **str** | JEDEC ID | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**node_device_id** | **int** | ID of the node | [optional] 
**node_id** | **str** | Unique Identifier of the node. | [optional] 
**node_memory_type** | **str** | Type of the physical memory | [optional] 
**part_number** | **str** | Part number | [optional] 
**request_uri** | **str** | requestUri for detailed node memory object | [optional] 
**resource_uri** | **str** | resourceUri for detailed node memory object | [optional] 
**revision** | **str** | Revision | [optional] 
**riser** | **str** | Riser | [optional] 
**size_mi_b** | **int** | Size in MiB | [optional] 
**slot** | **int** | Slot of the node physical memory | [optional] 
**slot_id** | **str** | Slot ID of the node physical memory | [optional] 
**system_id** | **str** | SystemId/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.node_memory_details import NodeMemoryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NodeMemoryDetails from a JSON string
node_memory_details_instance = NodeMemoryDetails.from_json(json)
# print the JSON string representation of the object
print(NodeMemoryDetails.to_json())

# convert the object into a dict
node_memory_details_dict = node_memory_details_instance.to_dict()
# create an instance of NodeMemoryDetails from a dict
node_memory_details_from_dict = NodeMemoryDetails.from_dict(node_memory_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


