# DeviceType4EnclosureCardDetailedFieldsEnclosureCardTpm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosureCardTpmDetails]**](DeviceType4enclosureCardTpmDetails.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of disks | [optional] 

## Example

```python
from dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_tpm import DeviceType4EnclosureCardDetailedFieldsEnclosureCardTpm

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosureCardDetailedFieldsEnclosureCardTpm from a JSON string
device_type4_enclosure_card_detailed_fields_enclosure_card_tpm_instance = DeviceType4EnclosureCardDetailedFieldsEnclosureCardTpm.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosureCardDetailedFieldsEnclosureCardTpm.to_json())

# convert the object into a dict
device_type4_enclosure_card_detailed_fields_enclosure_card_tpm_dict = device_type4_enclosure_card_detailed_fields_enclosure_card_tpm_instance.to_dict()
# create an instance of DeviceType4EnclosureCardDetailedFieldsEnclosureCardTpm from a dict
device_type4_enclosure_card_detailed_fields_enclosure_card_tpm_from_dict = DeviceType4EnclosureCardDetailedFieldsEnclosureCardTpm.from_dict(device_type4_enclosure_card_detailed_fields_enclosure_card_tpm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


