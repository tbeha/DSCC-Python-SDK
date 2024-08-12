# DeviceType4enclosureCardFanDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | **str** | Enclosure status code. | [optional] 
**enclosure_card_fan_id** | **int** | Numeric ID of the resource | [optional] 
**enclosure_card_id** | **int** | Numeric ID of the resource | [optional] 
**enclosure_card_uid** | **str** | Enclosure Card UID of the resource. | [optional] 
**enclosure_id** | **int** | Numeric ID of the resource | [optional] 
**enclosure_name** | **str** | Name of the enclosure | [optional] 
**enclosure_type** | [**DeviceType4enclosureTypeSingle**](DeviceType4enclosureTypeSingle.md) |  | [optional] 
**enclosure_uid** | **str** | Enclosure UID of the resource. | [optional] 
**fail_indicator** | **bool** |  | [optional] 
**fan_id** | **str** | SystemUid/Serial Number  of the array.This is deprecated. | [optional] 
**fan_uid** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. | [optional] 
**manufacturing** | [**DeviceType4ManufacturingSingle**](DeviceType4ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**speed** | **str** | Speed of the resource | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_card_fan_details import DeviceType4enclosureCardFanDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureCardFanDetails from a JSON string
device_type4enclosure_card_fan_details_instance = DeviceType4enclosureCardFanDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureCardFanDetails.to_json())

# convert the object into a dict
device_type4enclosure_card_fan_details_dict = device_type4enclosure_card_fan_details_instance.to_dict()
# create an instance of DeviceType4enclosureCardFanDetails from a dict
device_type4enclosure_card_fan_details_from_dict = DeviceType4enclosureCardFanDetails.from_dict(device_type4enclosure_card_fan_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


