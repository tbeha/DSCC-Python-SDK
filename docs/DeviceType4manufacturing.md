# DeviceType4manufacturing

Manufacturing information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly_rev** | **str** | Assembly revision | [optional] 
**check_sum** | **str** | Checksum | [optional] 
**hpe_model_name** | **str** | HPE model name | [optional] 
**manufacturer** | **str** | Manufacturer. &#x60;Filter, Sort&#x60; | [optional] 
**model** | **str** | Model | [optional] 
**saleable_part_number** | **str** | Saleable part number | [optional] 
**saleable_serial_number** | **str** | Saleable serial number | [optional] 
**serial_number** | **str** | Serial number. &#x60;Filter, Sort&#x60; | [optional] 
**spare_part_number** | **str** | Spare part number | [optional] 

## Example

```python
from dscc.models.device_type4manufacturing import DeviceType4manufacturing

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4manufacturing from a JSON string
device_type4manufacturing_instance = DeviceType4manufacturing.from_json(json)
# print the JSON string representation of the object
print(DeviceType4manufacturing.to_json())

# convert the object into a dict
device_type4manufacturing_dict = device_type4manufacturing_instance.to_dict()
# create an instance of DeviceType4manufacturing from a dict
device_type4manufacturing_from_dict = DeviceType4manufacturing.from_dict(device_type4manufacturing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


