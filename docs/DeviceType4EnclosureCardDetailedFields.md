# DeviceType4EnclosureCardDetailedFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dcsdata** | [**DeviceType4ecDcsdata**](DeviceType4ecDcsdata.md) |  | [optional] 
**displayname** | **str** | Enclosure Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**element_status_code** | **str** | Enclosure status code | [optional] 
**enclosure_card_boot_drives** | [**DeviceType4EnclosureCardDetailedFieldsEnclosureCardBootDrives**](DeviceType4EnclosureCardDetailedFieldsEnclosureCardBootDrives.md) |  | [optional] 
**enclosure_card_cpu** | [**DeviceType4EnclosureCardDetailedFieldsEnclosureCardCpu**](DeviceType4EnclosureCardDetailedFieldsEnclosureCardCpu.md) |  | [optional] 
**enclosure_card_fan** | [**DeviceType4EnclosureCardDetailedFieldsEnclosureCardFan**](DeviceType4EnclosureCardDetailedFieldsEnclosureCardFan.md) |  | [optional] 
**enclosure_card_id** | **int** | ID of enclosure card. | [optional] 
**enclosure_card_mem** | [**DeviceType4EnclosureCardDetailedFieldsEnclosureCardMem**](DeviceType4EnclosureCardDetailedFieldsEnclosureCardMem.md) |  | [optional] 
**enclosure_card_pci** | [**DeviceType4EnclosureCardDetailedFieldsEnclosureCardPci**](DeviceType4EnclosureCardDetailedFieldsEnclosureCardPci.md) |  | [optional] 
**enclosure_card_tpm** | [**DeviceType4EnclosureCardDetailedFieldsEnclosureCardTpm**](DeviceType4EnclosureCardDetailedFieldsEnclosureCardTpm.md) |  | [optional] 
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
**request_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**resource_uri** | **str** | resourceUri for detailed enclosure object | [optional] 
**safe_to_remove** | **bool** |  | [optional] 
**seven_seg_display** | **str** | Seven segment display | [optional] 
**state** | [**DeviceType4State**](DeviceType4State.md) |  | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.device_type4_enclosure_card_detailed_fields import DeviceType4EnclosureCardDetailedFields

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosureCardDetailedFields from a JSON string
device_type4_enclosure_card_detailed_fields_instance = DeviceType4EnclosureCardDetailedFields.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosureCardDetailedFields.to_json())

# convert the object into a dict
device_type4_enclosure_card_detailed_fields_dict = device_type4_enclosure_card_detailed_fields_instance.to_dict()
# create an instance of DeviceType4EnclosureCardDetailedFields from a dict
device_type4_enclosure_card_detailed_fields_from_dict = DeviceType4EnclosureCardDetailedFields.from_dict(device_type4_enclosure_card_detailed_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


