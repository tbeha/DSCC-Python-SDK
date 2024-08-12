# EnclosureDiskList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dc4data** | [**EdDc4data**](EdDc4data.md) |  | [optional] 
**dcsdata** | [**EdDcsdata**](EdDcsdata.md) |  | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure_device_id** | **int** |  | [optional] 
**enclosure_id** | **str** | Parent UID of the resource. &#x60;Filter&#x60; | [optional] 
**enclosure_name** | **str** | Name of the enclosure | [optional] 
**enclosure_type** | [**EnclosureType**](EnclosureType.md) |  | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**loop_a** | [**EnclosureDiskLoop**](EnclosureDiskLoop.md) |  | [optional] 
**loop_b** | [**EnclosureDiskLoop**](EnclosureDiskLoop.md) |  | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**position** | [**DiskPosition**](DiskPosition.md) |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure disk object | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**temperature** | **int** | temperature of the resource part | [optional] 
**type** | **str** | type | [optional] 
**wwn** | **str** | WWN of the resource. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.enclosure_disk_list import EnclosureDiskList

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosureDiskList from a JSON string
enclosure_disk_list_instance = EnclosureDiskList.from_json(json)
# print the JSON string representation of the object
print(EnclosureDiskList.to_json())

# convert the object into a dict
enclosure_disk_list_dict = enclosure_disk_list_instance.to_dict()
# create an instance of EnclosureDiskList from a dict
enclosure_disk_list_from_dict = EnclosureDiskList.from_dict(enclosure_disk_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


