# NodeDrivesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**fw_version** | **str** | Firmware version | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**manufacturing** | [**Manufacturing**](Manufacturing.md) |  | [optional] 
**max_lba** | **str** | Max Logical Block Address | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**node_device_id** | **int** | ID of the node | [optional] 
**node_drive_id** | **int** | Numeric ID of the resource | [optional] 
**node_drive_type** | **str** | Node type | [optional] 
**node_id** | **str** | Unique Identifier of the node. &#x60;Filter, Sort&#x60; | [optional] 
**resource_uri** | **str** | resourceUri for detailed node object | [optional] 
**sed_state** | **str** | SED state | [optional] 
**size_mi_b** | **int** | Size in MiB. &#x60;Filter, Sort&#x60; | [optional] 
**system_id** | **str** | SystemId/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 
**wwn** | **str** | Unique World Wide Name | [optional] 

## Example

```python
from dscc.models.node_drives_list import NodeDrivesList

# TODO update the JSON string below
json = "{}"
# create an instance of NodeDrivesList from a JSON string
node_drives_list_instance = NodeDrivesList.from_json(json)
# print the JSON string representation of the object
print(NodeDrivesList.to_json())

# convert the object into a dict
node_drives_list_dict = node_drives_list_instance.to_dict()
# create an instance of NodeDrivesList from a dict
node_drives_list_from_dict = NodeDrivesList.from_dict(node_drives_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


