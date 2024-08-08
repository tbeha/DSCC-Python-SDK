# DeviceType4cpgGrow

CPG grow information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **str** | The admin/data LD creation arguments used by the CPG when growing new LDs | [optional] 
**limit_mi_b** | **float** | Limit size in MiB beyond which the admin/data space will not grow | [optional] 
**size_mi_b** | **float** | Amount of admin/data LD storage in MiB created on each auto-grow | [optional] 
**warn_mi_b** | **float** | Size in MiB of the admin/data space at which a warning alert is generated | [optional] 

## Example

```python
from dscc.models.device_type4cpg_grow import DeviceType4cpgGrow

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4cpgGrow from a JSON string
device_type4cpg_grow_instance = DeviceType4cpgGrow.from_json(json)
# print the JSON string representation of the object
print(DeviceType4cpgGrow.to_json())

# convert the object into a dict
device_type4cpg_grow_dict = device_type4cpg_grow_instance.to_dict()
# create an instance of DeviceType4cpgGrow from a dict
device_type4cpg_grow_from_dict = DeviceType4cpgGrow.from_dict(device_type4cpg_grow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


