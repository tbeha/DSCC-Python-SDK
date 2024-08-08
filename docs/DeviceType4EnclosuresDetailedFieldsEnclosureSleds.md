# DeviceType4EnclosuresDetailedFieldsEnclosureSleds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosureSledLists]**](DeviceType4enclosureSledLists.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of enclosureSleds | [optional] 

## Example

```python
from dscc.models.device_type4_enclosures_detailed_fields_enclosure_sleds import DeviceType4EnclosuresDetailedFieldsEnclosureSleds

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosuresDetailedFieldsEnclosureSleds from a JSON string
device_type4_enclosures_detailed_fields_enclosure_sleds_instance = DeviceType4EnclosuresDetailedFieldsEnclosureSleds.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosuresDetailedFieldsEnclosureSleds.to_json())

# convert the object into a dict
device_type4_enclosures_detailed_fields_enclosure_sleds_dict = device_type4_enclosures_detailed_fields_enclosure_sleds_instance.to_dict()
# create an instance of DeviceType4EnclosuresDetailedFieldsEnclosureSleds from a dict
device_type4_enclosures_detailed_fields_enclosure_sleds_from_dict = DeviceType4EnclosuresDetailedFieldsEnclosureSleds.from_dict(device_type4_enclosures_detailed_fields_enclosure_sleds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


