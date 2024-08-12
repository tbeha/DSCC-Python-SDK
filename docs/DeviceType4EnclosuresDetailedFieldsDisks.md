# DeviceType4EnclosuresDetailedFieldsDisks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4disksLists]**](DeviceType4disksLists.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of disks | [optional] 

## Example

```python
from dscc.models.device_type4_enclosures_detailed_fields_disks import DeviceType4EnclosuresDetailedFieldsDisks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosuresDetailedFieldsDisks from a JSON string
device_type4_enclosures_detailed_fields_disks_instance = DeviceType4EnclosuresDetailedFieldsDisks.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosuresDetailedFieldsDisks.to_json())

# convert the object into a dict
device_type4_enclosures_detailed_fields_disks_dict = device_type4_enclosures_detailed_fields_disks_instance.to_dict()
# create an instance of DeviceType4EnclosuresDetailedFieldsDisks from a dict
device_type4_enclosures_detailed_fields_disks_from_dict = DeviceType4EnclosuresDetailedFieldsDisks.from_dict(device_type4_enclosures_detailed_fields_disks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


