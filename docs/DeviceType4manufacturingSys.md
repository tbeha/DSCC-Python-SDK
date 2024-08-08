# DeviceType4manufacturingSys

Manufacturing information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly_rev** | **str** | Assembly revision | [optional] 
**check_sum** | **str** | Checksum | [optional] 
**hpe_model_name** | **str** | HPE model name | [optional] 
**manufacturer** | **str** | Manufacturer &#x60;Filter&#x60; | [optional] 
**model** | **str** | Model &#x60;Filter&#x60; | [optional] 
**saleable_part_number** | **str** | Saleable part number | [optional] 
**saleable_serial_number** | **str** | Saleable serial number | [optional] 
**serial_number** | **str** | Serial number &#x60;Filter, Sort&#x60; | [optional] 
**spare_part_number** | **str** | Spare part number | [optional] 

## Example

```python
from dscc.models.device_type4manufacturing_sys import DeviceType4manufacturingSys

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4manufacturingSys from a JSON string
device_type4manufacturing_sys_instance = DeviceType4manufacturingSys.from_json(json)
# print the JSON string representation of the object
print(DeviceType4manufacturingSys.to_json())

# convert the object into a dict
device_type4manufacturing_sys_dict = device_type4manufacturing_sys_instance.to_dict()
# create an instance of DeviceType4manufacturingSys from a dict
device_type4manufacturing_sys_from_dict = DeviceType4manufacturingSys.from_dict(device_type4manufacturing_sys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


