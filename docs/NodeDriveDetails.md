# NodeDriveDetails


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
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**max_lba** | **str** | Max Logical Block Address | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**node_device_id** | **int** | ID of the node | [optional] 
**node_drive_id** | **int** | Numeric ID of the resource | [optional] 
**node_drive_type** | **str** | Node type | [optional] 
**node_id** | **str** | Unique Identifier of the node. | [optional] 
**request_uri** | **str** | requestUri for detailed node object | [optional] 
**resource_uri** | **str** | resourceUri for detailed node object | [optional] 
**sed_state** | **str** | SED state | [optional] 
**size_mi_b** | **int** | Size in MiB. | [optional] 
**system_id** | **str** | SystemId/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 
**wwn** | **str** | Unique World Wide Name | [optional] 

## Example

```python
from dscc.models.node_drive_details import NodeDriveDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NodeDriveDetails from a JSON string
node_drive_details_instance = NodeDriveDetails.from_json(json)
# print the JSON string representation of the object
print(NodeDriveDetails.to_json())

# convert the object into a dict
node_drive_details_dict = node_drive_details_instance.to_dict()
# create an instance of NodeDriveDetails from a dict
node_drive_details_from_dict = NodeDriveDetails.from_dict(node_drive_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


