# DeviceType4EnclosuresDetailedFieldsEnclosurePowerSupplies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceType4enclosurePowersLists]**](DeviceType4enclosurePowersLists.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**total** | **int** | Number of enclosurePowerSupplies | [optional] 

## Example

```python
from dscc.models.device_type4_enclosures_detailed_fields_enclosure_power_supplies import DeviceType4EnclosuresDetailedFieldsEnclosurePowerSupplies

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EnclosuresDetailedFieldsEnclosurePowerSupplies from a JSON string
device_type4_enclosures_detailed_fields_enclosure_power_supplies_instance = DeviceType4EnclosuresDetailedFieldsEnclosurePowerSupplies.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EnclosuresDetailedFieldsEnclosurePowerSupplies.to_json())

# convert the object into a dict
device_type4_enclosures_detailed_fields_enclosure_power_supplies_dict = device_type4_enclosures_detailed_fields_enclosure_power_supplies_instance.to_dict()
# create an instance of DeviceType4EnclosuresDetailedFieldsEnclosurePowerSupplies from a dict
device_type4_enclosures_detailed_fields_enclosure_power_supplies_from_dict = DeviceType4EnclosuresDetailedFieldsEnclosurePowerSupplies.from_dict(device_type4_enclosures_detailed_fields_enclosure_power_supplies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


