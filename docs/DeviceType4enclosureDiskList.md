# DeviceType4enclosureDiskList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dc4data** | [**DeviceType4edDc4data**](DeviceType4edDc4data.md) |  | [optional] 
**dcsdata** | [**DeviceType4edDcsdata**](DeviceType4edDcsdata.md) |  | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**enclosure_id** | **int** |  | [optional] 
**enclosure_name** | **str** | Name of the enclosure | [optional] 
**enclosure_type** | [**DeviceType4enclosureType**](DeviceType4enclosureType.md) |  | [optional] 
**enclosure_uid** | **str** | Parent UID of the resource. &#x60;Filter&#x60; | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**loop_a** | [**DeviceType4enclosureDiskLoop**](DeviceType4enclosureDiskLoop.md) |  | [optional] 
**loop_b** | [**DeviceType4enclosureDiskLoop**](DeviceType4enclosureDiskLoop.md) |  | [optional] 
**manufacturing** | [**DeviceType4EnclosureDiskDetailsManufacturing**](DeviceType4EnclosureDiskDetailsManufacturing.md) |  | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**position** | [**DeviceType4diskPosition**](DeviceType4diskPosition.md) |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure disk object | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**temperature** | **int** | temperature of the resource part. This field is deprecated. | [optional] 
**type** | **str** | type | [optional] 
**wwn** | **str** | WWN of the resource. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_disk_list import DeviceType4enclosureDiskList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureDiskList from a JSON string
device_type4enclosure_disk_list_instance = DeviceType4enclosureDiskList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureDiskList.to_json())

# convert the object into a dict
device_type4enclosure_disk_list_dict = device_type4enclosure_disk_list_instance.to_dict()
# create an instance of DeviceType4enclosureDiskList from a dict
device_type4enclosure_disk_list_from_dict = DeviceType4enclosureDiskList.from_dict(device_type4enclosure_disk_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


