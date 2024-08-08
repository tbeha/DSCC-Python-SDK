# EnclosureFanDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | **str** | Enclosure status code. | [optional] 
**enclosure_cooling_fan_id** | **int** | Numeric ID of the resource | [optional] 
**enclosure_device_id** | **int** |  | [optional] 
**enclosure_id** | **str** | Parent UID of the resource. | [optional] 
**enclosure_name** | **str** | Name of the enclosure | [optional] 
**enclosure_type** | [**EnclosureTypeSingle**](EnclosureTypeSingle.md) |  | [optional] 
**fail_indicator** | **bool** |  | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**part_number** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**ps_id** | **int** |  | [optional] 
**request_uri** | **str** | resourceUri for detailed enclosure fan object | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure fan object | [optional] 
**safe_to_remove** | **bool** |  | [optional] 
**speed** | **str** | Speed of the resource | [optional] 
**speed_rpm** | **int** | Speed in rpm | [optional] 
**state** | [**STATE**](STATE.md) |  | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 
**wwn** | **str** |  | [optional] 

## Example

```python
from dscc.models.enclosure_fan_details import EnclosureFanDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EnclosureFanDetails from a JSON string
enclosure_fan_details_instance = EnclosureFanDetails.from_json(json)
# print the JSON string representation of the object
print(EnclosureFanDetails.to_json())

# convert the object into a dict
enclosure_fan_details_dict = enclosure_fan_details_instance.to_dict()
# create an instance of EnclosureFanDetails from a dict
enclosure_fan_details_from_dict = EnclosureFanDetails.from_dict(enclosure_fan_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


