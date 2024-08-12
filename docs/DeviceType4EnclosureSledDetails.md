# DeviceType4EnclosureSledDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dc4data** | [**DeviceType4dc4dataSingle**](DeviceType4dc4dataSingle.md) |  | [optional] 
**disk_count** | **int** | Number of disks present | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | **str** | Enclosure status code | [optional] 
**enclosure_id** | **int** |  | [optional] 
**enclosure_name** | **str** | Name of the enclosure | [optional] 
**enclosure_type** | [**DeviceType4enclosureTypeSingle**](DeviceType4enclosureTypeSingle.md) |  | [optional] 
**enclosure_uid** | **str** | Parent UID of the resource. | [optional] 
**fail_indicator** | **bool** |  | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**manufacturing** | [**DeviceType4ManufacturingSingle**](DeviceType4ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**ok_indicator** | **bool** |  | [optional] 
**port_bypass_a** | **bool** |  | [optional] 
**port_bypass_b** | **bool** |  | [optional] 
**power** | **bool** |  | [optional] 
**pred_fail_indicator** | **bool** |  | [optional] 
**protocol** | **str** |  | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
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
from dscc.models.device_type4_enclosure_sled_details import DeviceType4EnclosureSledDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosureSledDetails from a JSON string
device_type4_enclosure_sled_details_instance = DeviceType4EnclosureSledDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosureSledDetails.to_json())

# convert the object into a dict
device_type4_enclosure_sled_details_dict = device_type4_enclosure_sled_details_instance.to_dict()
# create an instance of DeviceType4EnclosureSledDetails from a dict
device_type4_enclosure_sled_details_from_dict = DeviceType4EnclosureSledDetails.from_dict(device_type4_enclosure_sled_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


