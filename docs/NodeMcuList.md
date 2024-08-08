# NodeMcuList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**fw_version** | **str** | Firmware version | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**model** | **str** | Model name | [optional] 
**name** | **str** | Name to be used for display purposes | [optional] 
**node_device_id** | **int** | ID of the node | [optional] 
**node_id** | **str** | Unique Identifier of the node. &#x60;Filter, Sort&#x60; | [optional] 
**reset_reason** | **str** | The reason why MicroController Unit was reset | [optional] 
**resource_uri** | **str** | resourceUri for detailed node mcu object | [optional] 
**state** | [**STATE**](STATE.md) |  | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 
**up_since** | [**Uptime**](Uptime.md) |  | [optional] 

## Example

```python
from dscc.models.node_mcu_list import NodeMcuList

# TODO update the JSON string below
json = "{}"
# create an instance of NodeMcuList from a JSON string
node_mcu_list_instance = NodeMcuList.from_json(json)
# print the JSON string representation of the object
print(NodeMcuList.to_json())

# convert the object into a dict
node_mcu_list_dict = node_mcu_list_instance.to_dict()
# create an instance of NodeMcuList from a dict
node_mcu_list_from_dict = NodeMcuList.from_dict(node_mcu_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


