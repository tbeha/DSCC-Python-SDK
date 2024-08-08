# EnclosureDiskDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dc4data** | [**EdDc4data**](EdDc4data.md) |  | [optional] 
**dcsdata** | [**EdDcsdata**](EdDcsdata.md) |  | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure_device_id** | **int** |  | [optional] 
**enclosure_id** | **str** | Parent UID of the resource. | [optional] 
**enclosure_name** | **str** | Name of the enclosure | [optional] 
**enclosure_type** | [**EnclosureTypeSingle**](EnclosureTypeSingle.md) |  | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. | [optional] 
**loop_a** | [**EnclosureDiskLoop**](EnclosureDiskLoop.md) |  | [optional] 
**loop_b** | [**EnclosureDiskLoop**](EnclosureDiskLoop.md) |  | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**position** | [**DiskPosition**](DiskPosition.md) |  | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**temperature** | **int** | temperature of the resource part | [optional] 
**type** | **str** | type | [optional] 
**wwn** | **str** | WWN of the resource. | [optional] 

## Example

```python
from dscc.models.enclosure_disk_details import EnclosureDiskDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosureDiskDetails from a JSON string
enclosure_disk_details_instance = EnclosureDiskDetails.from_json(json)
# print the JSON string representation of the object
print(EnclosureDiskDetails.to_json())

# convert the object into a dict
enclosure_disk_details_dict = enclosure_disk_details_instance.to_dict()
# create an instance of EnclosureDiskDetails from a dict
enclosure_disk_details_from_dict = EnclosureDiskDetails.from_dict(enclosure_disk_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


