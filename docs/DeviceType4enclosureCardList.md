# DeviceType4enclosureCardList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dcsdata** | [**DeviceType4ecDcsdata**](DeviceType4ecDcsdata.md) |  | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | **str** | Enclosure status code | [optional] 
**enclosure_card_id** | **int** | ID of enclosure card. | [optional] 
**enclosure_id** | **int** |  | [optional] 
**enclosure_name** | **str** | Name of the enclosure. &#x60;Filter, Sort&#x60; | [optional] 
**enclosure_type** | [**DeviceType4enclosureTypeSingle**](DeviceType4enclosureTypeSingle.md) |  | [optional] 
**enclosure_uid** | **str** | Parent UID of the resource. &#x60;Filter&#x60; | [optional] 
**fail_indicator** | **bool** |  | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**is_node_card** | **bool** |  | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**locate_seven_seg_display** | **str** | Seven segment display on enclosure card when locate is on | [optional] 
**loop_a** | **bool** |  | [optional] 
**loop_b** | **bool** |  | [optional] 
**manufacturing** | [**DeviceType4manufacturing**](DeviceType4manufacturing.md) |  | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure card object | [optional] 
**safe_to_remove** | **bool** |  | [optional] 
**seven_seg_display** | **str** | Seven segment display | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_card_list import DeviceType4enclosureCardList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureCardList from a JSON string
device_type4enclosure_card_list_instance = DeviceType4enclosureCardList.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureCardList.to_json())

# convert the object into a dict
device_type4enclosure_card_list_dict = device_type4enclosure_card_list_instance.to_dict()
# create an instance of DeviceType4enclosureCardList from a dict
device_type4enclosure_card_list_from_dict = DeviceType4enclosureCardList.from_dict(device_type4enclosure_card_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


