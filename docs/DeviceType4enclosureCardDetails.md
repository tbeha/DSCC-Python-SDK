# DeviceType4enclosureCardDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | customerId | [optional] 
**dcsdata** | [**DeviceType4ecDcsdata**](DeviceType4ecDcsdata.md) |  | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | **str** | Enclosure status code | [optional] 
**enclosure_card_id** | **int** | ID of enclosure card. | [optional] 
**enclosure_id** | **int** |  | [optional] 
**enclosure_name** | **str** | Name of the enclosure. | [optional] 
**enclosure_type** | [**DeviceType4enclosureTypeSingle**](DeviceType4enclosureTypeSingle.md) |  | [optional] 
**enclosure_uid** | **str** | Parent UID of the resource. | [optional] 
**fail_indicator** | **bool** |  | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Unique Identifier of the resource. | [optional] 
**is_node_card** | **bool** |  | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**locate_seven_seg_display** | **str** | Seven segment display on enclosure card when locate is on | [optional] 
**loop_a** | **bool** |  | [optional] 
**loop_b** | **bool** |  | [optional] 
**manufacturing** | [**DeviceType4ManufacturingSingle**](DeviceType4ManufacturingSingle.md) |  | [optional] 
**name** | **str** | Name of the resource. | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**safe_to_remove** | **bool** |  | [optional] 
**seven_seg_display** | **str** | Seven segment display | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_card_details import DeviceType4enclosureCardDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureCardDetails from a JSON string
device_type4enclosure_card_details_instance = DeviceType4enclosureCardDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureCardDetails.to_json())

# convert the object into a dict
device_type4enclosure_card_details_dict = device_type4enclosure_card_details_instance.to_dict()
# create an instance of DeviceType4enclosureCardDetails from a dict
device_type4enclosure_card_details_from_dict = DeviceType4enclosureCardDetails.from_dict(device_type4enclosure_card_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


