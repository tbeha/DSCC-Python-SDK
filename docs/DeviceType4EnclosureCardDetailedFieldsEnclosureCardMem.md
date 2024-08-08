# DeviceType4EnclosureCardDetailedFieldsEnclosureCardMem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosureCardMemoryDetails]**](DeviceType4enclosureCardMemoryDetails.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of disks | [optional] 

## Example

```python
from dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_mem import DeviceType4EnclosureCardDetailedFieldsEnclosureCardMem

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosureCardDetailedFieldsEnclosureCardMem from a JSON string
device_type4_enclosure_card_detailed_fields_enclosure_card_mem_instance = DeviceType4EnclosureCardDetailedFieldsEnclosureCardMem.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosureCardDetailedFieldsEnclosureCardMem.to_json())

# convert the object into a dict
device_type4_enclosure_card_detailed_fields_enclosure_card_mem_dict = device_type4_enclosure_card_detailed_fields_enclosure_card_mem_instance.to_dict()
# create an instance of DeviceType4EnclosureCardDetailedFieldsEnclosureCardMem from a dict
device_type4_enclosure_card_detailed_fields_enclosure_card_mem_from_dict = DeviceType4EnclosureCardDetailedFieldsEnclosureCardMem.from_dict(device_type4_enclosure_card_detailed_fields_enclosure_card_mem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


