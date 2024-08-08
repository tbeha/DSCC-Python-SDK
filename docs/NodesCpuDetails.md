# NodesCpuDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**bus_speed** | **float** | Bus speed in Mhz | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**family** | **str** | Family | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**node_cpu_id** | **int** | Numeric ID of the resource | [optional] 
**node_device_id** | **int** | ID of the node | [optional] 
**node_id** | **str** | Unique Identifier of the node. | [optional] 
**request_uri** | **str** | requestUri for detailed node Cpu object | [optional] 
**resource_uri** | **str** | resourceUri for detailed node cpu object | [optional] 
**speed** | **int** | Speed in Mhz | [optional] 
**stepping** | **str** | Stepping level | [optional] 
**system_id** | **str** | systemId/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.nodes_cpu_details import NodesCpuDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NodesCpuDetails from a JSON string
nodes_cpu_details_instance = NodesCpuDetails.from_json(json)
# print the JSON string representation of the object
print(NodesCpuDetails.to_json())

# convert the object into a dict
nodes_cpu_details_dict = nodes_cpu_details_instance.to_dict()
# create an instance of NodesCpuDetails from a dict
nodes_cpu_details_from_dict = NodesCpuDetails.from_dict(nodes_cpu_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


