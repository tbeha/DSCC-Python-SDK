# DeviceType4NodeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure_card_id** | **int** | ID of the enclosure card | [optional] 
**enclosure_card_uid** | **str** | Unique Identifier of the enclosure card | [optional] 
**enclosure_id** | **int** | ID of the enclosure | [optional] 
**enclosure_uid** | **str** | Unique Identifier of the enclosure &#x60;Filter&#x60; | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. | [optional] 
**in_cluster** | **bool** | Indicates if this node is part of the cluster. | [optional] 
**kernel_version** | **str** | Kernel version | [optional] 
**master** | **bool** | Indicates if this is the master node. | [optional] 
**memory_mi_b** | **int** | Total data memory in the node in MiB | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**online** | **bool** | Indicates if this node is online | [optional] 
**request_uri** | **str** | requestUri for detailed node object | [optional] 
**resource_uri** | **str** | resourceUri for detailed node object | [optional] 
**safe_to_remove** | **bool** | Indicates if the component is safe to remove | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**system_id** | **str** | SystemId/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 
**uptime** | [**DeviceType4uptime**](DeviceType4uptime.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_node_details import DeviceType4NodeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4NodeDetails from a JSON string
device_type4_node_details_instance = DeviceType4NodeDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4NodeDetails.to_json())

# convert the object into a dict
device_type4_node_details_dict = device_type4_node_details_instance.to_dict()
# create an instance of DeviceType4NodeDetails from a dict
device_type4_node_details_from_dict = DeviceType4NodeDetails.from_dict(device_type4_node_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


