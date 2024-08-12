# DeviceType4EnclosureCardDetailedFieldsEnclosureCardFan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosureCardFanDetails]**](DeviceType4enclosureCardFanDetails.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of disks | [optional] 

## Example

```python
from dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_fan import DeviceType4EnclosureCardDetailedFieldsEnclosureCardFan

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosureCardDetailedFieldsEnclosureCardFan from a JSON string
device_type4_enclosure_card_detailed_fields_enclosure_card_fan_instance = DeviceType4EnclosureCardDetailedFieldsEnclosureCardFan.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosureCardDetailedFieldsEnclosureCardFan.to_json())

# convert the object into a dict
device_type4_enclosure_card_detailed_fields_enclosure_card_fan_dict = device_type4_enclosure_card_detailed_fields_enclosure_card_fan_instance.to_dict()
# create an instance of DeviceType4EnclosureCardDetailedFieldsEnclosureCardFan from a dict
device_type4_enclosure_card_detailed_fields_enclosure_card_fan_from_dict = DeviceType4EnclosureCardDetailedFieldsEnclosureCardFan.from_dict(device_type4_enclosure_card_detailed_fields_enclosure_card_fan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


