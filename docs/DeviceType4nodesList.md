# DeviceType4nodesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure_card_id** | **int** | ID of the enclosure card | [optional] 
**enclosure_card_uid** | **str** | Unique Identifier of the enclosure card &#x60;Filter&#x60; | [optional] 
**enclosure_id** | **int** | ID of the enclosure | [optional] 
**enclosure_uid** | **str** | Unique Identifier of the enclosure &#x60;Filter&#x60; | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**in_cluster** | **bool** | Indicates if this node is part of the cluster. | [optional] 
**kernel_version** | **str** | Kernel version | [optional] 
**master** | **bool** | Indicates if this is the master node. | [optional] 
**memory_mi_b** | **int** | Total data memory in the node in MiB | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**node_id** | **int** | Numeric ID of the resource. | [optional] 
**online** | **bool** | Indicates if this node is online | [optional] 
**resource_uri** | **str** | resourceUri for detailed node object | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**system_id** | **str** | SystemId/serialNumber of the array. | [optional] 
**type** | **str** | type | [optional] 
**uptime** | [**DeviceType4uptime**](DeviceType4uptime.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4nodes_list import DeviceType4nodesList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4nodesList from a JSON string
device_type4nodes_list_instance = DeviceType4nodesList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4nodesList.to_json())

# convert the object into a dict
device_type4nodes_list_dict = device_type4nodes_list_instance.to_dict()
# create an instance of DeviceType4nodesList from a dict
device_type4nodes_list_from_dict = DeviceType4nodesList.from_dict(device_type4nodes_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


