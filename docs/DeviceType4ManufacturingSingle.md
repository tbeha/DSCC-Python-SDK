# DeviceType4ManufacturingSingle

Manufacturing information

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
**serial_number** | **str** | Serial number. | [optional] 
**spare_part_number** | **str** | Spare part number | [optional] 

## Example

```python
from dscc.models.device_type4_manufacturing_single import DeviceType4ManufacturingSingle

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ManufacturingSingle from a JSON string
device_type4_manufacturing_single_instance = DeviceType4ManufacturingSingle.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ManufacturingSingle.to_json())

# convert the object into a dict
device_type4_manufacturing_single_dict = device_type4_manufacturing_single_instance.to_dict()
# create an instance of DeviceType4ManufacturingSingle from a dict
device_type4_manufacturing_single_from_dict = DeviceType4ManufacturingSingle.from_dict(device_type4_manufacturing_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


