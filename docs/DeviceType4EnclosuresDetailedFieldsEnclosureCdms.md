# DeviceType4EnclosuresDetailedFieldsEnclosureCdms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosureCdmDetails]**](DeviceType4enclosureCdmDetails.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of enclosureCdms | [optional] 

## Example

```python
from dscc.models.device_type4_enclosures_detailed_fields_enclosure_cdms import DeviceType4EnclosuresDetailedFieldsEnclosureCdms

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosuresDetailedFieldsEnclosureCdms from a JSON string
device_type4_enclosures_detailed_fields_enclosure_cdms_instance = DeviceType4EnclosuresDetailedFieldsEnclosureCdms.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosuresDetailedFieldsEnclosureCdms.to_json())

# convert the object into a dict
device_type4_enclosures_detailed_fields_enclosure_cdms_dict = device_type4_enclosures_detailed_fields_enclosure_cdms_instance.to_dict()
# create an instance of DeviceType4EnclosuresDetailedFieldsEnclosureCdms from a dict
device_type4_enclosures_detailed_fields_enclosure_cdms_from_dict = DeviceType4EnclosuresDetailedFieldsEnclosureCdms.from_dict(device_type4_enclosures_detailed_fields_enclosure_cdms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


