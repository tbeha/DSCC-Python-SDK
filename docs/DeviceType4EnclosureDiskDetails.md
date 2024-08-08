# DeviceType4EnclosureDiskDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dc4data** | [**DeviceType4edDc4data**](DeviceType4edDc4data.md) |  | [optional] 
**dcsdata** | [**DeviceType4edDcsdata**](DeviceType4edDcsdata.md) |  | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure_id** | **int** |  | [optional] 
**enclosure_name** | **str** | Name of the enclosure | [optional] 
**enclosure_type** | [**DeviceType4enclosureTypeSingle**](DeviceType4enclosureTypeSingle.md) |  | [optional] 
**enclosure_uid** | **str** | Parent UID of the resource. | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. | [optional] 
**loop_a** | [**DeviceType4enclosureDiskLoop**](DeviceType4enclosureDiskLoop.md) |  | [optional] 
**loop_b** | [**DeviceType4enclosureDiskLoop**](DeviceType4enclosureDiskLoop.md) |  | [optional] 
**manufacturing** | [**DeviceType4EnclosureDiskDetailsManufacturing**](DeviceType4EnclosureDiskDetailsManufacturing.md) |  | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**position** | [**DeviceType4diskPosition**](DeviceType4diskPosition.md) |  | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**temperature** | **int** | temperature of the resource part. This field is deprecated. | [optional] 
**type** | **str** | type | [optional] 
**wwn** | **str** | WWN of the resource. | [optional] 

## Example

```python
from dscc.models.device_type4_enclosure_disk_details import DeviceType4EnclosureDiskDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosureDiskDetails from a JSON string
device_type4_enclosure_disk_details_instance = DeviceType4EnclosureDiskDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosureDiskDetails.to_json())

# convert the object into a dict
device_type4_enclosure_disk_details_dict = device_type4_enclosure_disk_details_instance.to_dict()
# create an instance of DeviceType4EnclosureDiskDetails from a dict
device_type4_enclosure_disk_details_from_dict = DeviceType4EnclosureDiskDetails.from_dict(device_type4_enclosure_disk_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


