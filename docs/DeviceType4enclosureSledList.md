# DeviceType4enclosureSledList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dc4data** | [**DeviceType4esDc4data**](DeviceType4esDc4data.md) |  | [optional] 
**disk_count** | **int** | Number of disks present | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | **str** | Enclosure status code | [optional] 
**enclosure_id** | **int** |  | [optional] 
**enclosure_name** | **str** | Name of the enclosure | [optional] 
**enclosure_type** | [**DeviceType4enclosureTypeSingle**](DeviceType4enclosureTypeSingle.md) |  | [optional] 
**enclosure_uid** | **str** | Parent UID of the resource. &#x60;Filter&#x60; | [optional] 
**fail_indicator** | **bool** |  | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**manufacturing** | [**DeviceType4ManufacturingSingle**](DeviceType4ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**ok_indicator** | **bool** |  | [optional] 
**port_bypass_a** | **bool** |  | [optional] 
**port_bypass_b** | **bool** |  | [optional] 
**power** | **bool** |  | [optional] 
**pred_fail_indicator** | **bool** |  | [optional] 
**protocol** | **str** |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure card object | [optional] 
**safe_to_remove** | **bool** |  | [optional] 
**sled_id** | **int** | Numeric ID of the resource | [optional] 
**state_loop_a** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**state_loop_b** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**temperature** | **int** |  | [optional] 
**type** | **str** | type | [optional] 
**wwn** | **str** |  | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_sled_list import DeviceType4enclosureSledList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureSledList from a JSON string
device_type4enclosure_sled_list_instance = DeviceType4enclosureSledList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureSledList.to_json())

# convert the object into a dict
device_type4enclosure_sled_list_dict = device_type4enclosure_sled_list_instance.to_dict()
# create an instance of DeviceType4enclosureSledList from a dict
device_type4enclosure_sled_list_from_dict = DeviceType4enclosureSledList.from_dict(device_type4enclosure_sled_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


