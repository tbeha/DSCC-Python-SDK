# DeviceType4EnclosureCardDetailedFieldsEnclosureCardPci


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosureCardPciDetails]**](DeviceType4enclosureCardPciDetails.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of disks | [optional] 

## Example

```python
from dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_pci import DeviceType4EnclosureCardDetailedFieldsEnclosureCardPci

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosureCardDetailedFieldsEnclosureCardPci from a JSON string
device_type4_enclosure_card_detailed_fields_enclosure_card_pci_instance = DeviceType4EnclosureCardDetailedFieldsEnclosureCardPci.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosureCardDetailedFieldsEnclosureCardPci.to_json())

# convert the object into a dict
device_type4_enclosure_card_detailed_fields_enclosure_card_pci_dict = device_type4_enclosure_card_detailed_fields_enclosure_card_pci_instance.to_dict()
# create an instance of DeviceType4EnclosureCardDetailedFieldsEnclosureCardPci from a dict
device_type4_enclosure_card_detailed_fields_enclosure_card_pci_from_dict = DeviceType4EnclosureCardDetailedFieldsEnclosureCardPci.from_dict(device_type4_enclosure_card_detailed_fields_enclosure_card_pci_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


