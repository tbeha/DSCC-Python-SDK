# DeviceType4enclosureDiskListsManufacturing

Manufacturing information. This object is deprecated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly_rev** | **str** | Assembly revision | [optional] 
**check_sum** | **str** | Checksum | [optional] 
**hpe_model_name** | **str** | HPE model name | [optional] 
**manufacturer** | **str** | Manufacturer. | [optional] 
**model** | **str** | Model | [optional] 
**saleable_part_number** | **str** | Saleable part number | [optional] 
**saleable_serial_number** | **str** | Saleable serial number | [optional] 
**serial_number** | **str** | Serial number.  | [optional] 
**spare_part_number** | **str** | Spare part number | [optional] 

## Example

```python
from dscc.models.device_type4enclosure_disk_lists_manufacturing import DeviceType4enclosureDiskListsManufacturing

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4enclosureDiskListsManufacturing from a JSON string
device_type4enclosure_disk_lists_manufacturing_instance = DeviceType4enclosureDiskListsManufacturing.from_json(json)
# print the JSON string representation of the object
print(DeviceType4enclosureDiskListsManufacturing.to_json())

# convert the object into a dict
device_type4enclosure_disk_lists_manufacturing_dict = device_type4enclosure_disk_lists_manufacturing_instance.to_dict()
# create an instance of DeviceType4enclosureDiskListsManufacturing from a dict
device_type4enclosure_disk_lists_manufacturing_from_dict = DeviceType4enclosureDiskListsManufacturing.from_dict(device_type4enclosure_disk_lists_manufacturing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


