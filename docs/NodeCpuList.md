# NodeCpuList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**bus_speed** | **float** | Bus speed in Mhz | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**family** | **str** | Family | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource &#x60;Filter&#x60; | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**node_cpu_id** | **int** | Numeric ID of the resource | [optional] 
**node_device_id** | **int** | ID of the node | [optional] 
**node_id** | **str** | Unique Identifier of the node. &#x60;Filter, Sort&#x60; | [optional] 
**resource_uri** | **str** | resourceUri for detailed node cpu object | [optional] 
**speed** | **int** | Speed in Mhz | [optional] 
**stepping** | **str** | Stepping level | [optional] 
**system_id** | **str** | systemId/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.node_cpu_list import NodeCpuList

# TODO update the JSON string below
json = "{}"
# create an instance of NodeCpuList from a JSON string
node_cpu_list_instance = NodeCpuList.from_json(json)
# print the JSON string representation of the object
print(NodeCpuList.to_json())

# convert the object into a dict
node_cpu_list_dict = node_cpu_list_instance.to_dict()
# create an instance of NodeCpuList from a dict
node_cpu_list_from_dict = NodeCpuList.from_dict(node_cpu_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


