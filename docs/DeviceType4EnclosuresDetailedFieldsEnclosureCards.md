# DeviceType4EnclosuresDetailedFieldsEnclosureCards


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosureCardDetails]**](DeviceType4enclosureCardDetails.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of enclosureCards | [optional] 

## Example

```python
from dscc.models.device_type4_enclosures_detailed_fields_enclosure_cards import DeviceType4EnclosuresDetailedFieldsEnclosureCards

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosuresDetailedFieldsEnclosureCards from a JSON string
device_type4_enclosures_detailed_fields_enclosure_cards_instance = DeviceType4EnclosuresDetailedFieldsEnclosureCards.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosuresDetailedFieldsEnclosureCards.to_json())

# convert the object into a dict
device_type4_enclosures_detailed_fields_enclosure_cards_dict = device_type4_enclosures_detailed_fields_enclosure_cards_instance.to_dict()
# create an instance of DeviceType4EnclosuresDetailedFieldsEnclosureCards from a dict
device_type4_enclosures_detailed_fields_enclosure_cards_from_dict = DeviceType4EnclosuresDetailedFieldsEnclosureCards.from_dict(device_type4_enclosures_detailed_fields_enclosure_cards_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


