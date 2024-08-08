# DeviceType4enclosureDiskLists


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**manufacturing** | [**DeviceType4enclosureDiskListsManufacturing**](DeviceType4enclosureDiskListsManufacturing.md) |  | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**position** | [**DeviceType4diskPosition**](DeviceType4diskPosition.md) |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**temperature** | **int** | temperature of the resource part. This field is deprecated. | [optional] 
**type** | **str** | type | [optional] 
**wwn** | **str** | WWN of the resource. | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_disk_lists import DeviceType4enclosureDiskLists

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureDiskLists from a JSON string
device_type4enclosure_disk_lists_instance = DeviceType4enclosureDiskLists.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureDiskLists.to_json())

# convert the object into a dict
device_type4enclosure_disk_lists_dict = device_type4enclosure_disk_lists_instance.to_dict()
# create an instance of DeviceType4enclosureDiskLists from a dict
device_type4enclosure_disk_lists_from_dict = DeviceType4enclosureDiskLists.from_dict(device_type4enclosure_disk_lists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


