# DeviceType4EnclosureCardDetailedFieldsEnclosureCardCpu


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosureCardCpuDetails]**](DeviceType4enclosureCardCpuDetails.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of disks | [optional] 

## Example

```python
from dscc.models.device_type4_enclosure_card_detailed_fields_enclosure_card_cpu import DeviceType4EnclosureCardDetailedFieldsEnclosureCardCpu

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosureCardDetailedFieldsEnclosureCardCpu from a JSON string
device_type4_enclosure_card_detailed_fields_enclosure_card_cpu_instance = DeviceType4EnclosureCardDetailedFieldsEnclosureCardCpu.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosureCardDetailedFieldsEnclosureCardCpu.to_json())

# convert the object into a dict
device_type4_enclosure_card_detailed_fields_enclosure_card_cpu_dict = device_type4_enclosure_card_detailed_fields_enclosure_card_cpu_instance.to_dict()
# create an instance of DeviceType4EnclosureCardDetailedFieldsEnclosureCardCpu from a dict
device_type4_enclosure_card_detailed_fields_enclosure_card_cpu_from_dict = DeviceType4EnclosureCardDetailedFieldsEnclosureCardCpu.from_dict(device_type4_enclosure_card_detailed_fields_enclosure_card_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


