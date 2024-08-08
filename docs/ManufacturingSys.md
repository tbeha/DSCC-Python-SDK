# ManufacturingSys

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
from dscc.models.manufacturing_sys import ManufacturingSys

# TODO update the JSON string below
json = "{}"
# create an instance of ManufacturingSys from a JSON string
manufacturing_sys_instance = ManufacturingSys.from_json(json)
# print the JSON string representation of the object
print(ManufacturingSys.to_json())

# convert the object into a dict
manufacturing_sys_dict = manufacturing_sys_instance.to_dict()
# create an instance of ManufacturingSys from a dict
manufacturing_sys_from_dict = ManufacturingSys.from_dict(manufacturing_sys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


