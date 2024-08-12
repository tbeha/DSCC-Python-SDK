# EnclosureFanList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | **str** | Enclosure status code. | [optional] 
**enclosure_cooling_fan_id** | **int** | Numeric ID of the resource | [optional] 
**enclosure_device_id** | **int** |  | [optional] 
**enclosure_id** | **str** | Parent UID of the resource. &#x60;Filter&#x60; | [optional] 
**enclosure_name** | **str** | Name of the enclosure | [optional] 
**enclosure_type** | [**EnclosureTypeSingle**](EnclosureTypeSingle.md) |  | [optional] 
**fail_indicator** | **bool** |  | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**part_number** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**ps_id** | **int** |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure card object | [optional] 
**safe_to_remove** | **bool** |  | [optional] 
**speed** | **str** | Speed of the resource | [optional] 
**speed_rpm** | **int** | Speed in rpm | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 
**wwn** | **str** |  | [optional] 

## Example

```python
from dscc.models.enclosure_fan_list import EnclosureFanList

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosureFanList from a JSON string
enclosure_fan_list_instance = EnclosureFanList.from_json(json)
# print the JSON string representation of the object
print(EnclosureFanList.to_json())

# convert the object into a dict
enclosure_fan_list_dict = enclosure_fan_list_instance.to_dict()
# create an instance of EnclosureFanList from a dict
enclosure_fan_list_from_dict = EnclosureFanList.from_dict(enclosure_fan_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


