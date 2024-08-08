# DeviceType4EnclosureCardDetailedFieldsEnclosureCardBootDrives


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosureCardBootDriveDetails]**](DeviceType4enclosureCardBootDriveDetails.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of disks | [optional] 

## Example

```python
from dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_boot_drives import DeviceType4EnclosureCardDetailedFieldsEnclosureCardBootDrives

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosureCardDetailedFieldsEnclosureCardBootDrives from a JSON string
device_type4_enclosure_card_detailed_fields_enclosure_card_boot_drives_instance = DeviceType4EnclosureCardDetailedFieldsEnclosureCardBootDrives.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosureCardDetailedFieldsEnclosureCardBootDrives.to_json())

# convert the object into a dict
device_type4_enclosure_card_detailed_fields_enclosure_card_boot_drives_dict = device_type4_enclosure_card_detailed_fields_enclosure_card_boot_drives_instance.to_dict()
# create an instance of DeviceType4EnclosureCardDetailedFieldsEnclosureCardBootDrives from a dict
device_type4_enclosure_card_detailed_fields_enclosure_card_boot_drives_from_dict = DeviceType4EnclosureCardDetailedFieldsEnclosureCardBootDrives.from_dict(device_type4_enclosure_card_detailed_fields_enclosure_card_boot_drives_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


