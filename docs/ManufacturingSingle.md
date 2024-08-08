# ManufacturingSingle

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
from dscc.models.manufacturing_single import ManufacturingSingle

# TODO update the JSON string below
json = "{}"
# create an instance of ManufacturingSingle from a JSON string
manufacturing_single_instance = ManufacturingSingle.from_json(json)
# print the JSON string representation of the object
print(ManufacturingSingle.to_json())

# convert the object into a dict
manufacturing_single_dict = manufacturing_single_instance.to_dict()
# create an instance of ManufacturingSingle from a dict
manufacturing_single_from_dict = ManufacturingSingle.from_dict(manufacturing_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


