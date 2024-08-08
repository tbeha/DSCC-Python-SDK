# DeviceType4space


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_mi_b** | **float** |  | [optional] 
**grown_mi_b** | **float** |  | [optional] 
**raw_reserved_mi_b** | **float** |  | [optional] 
**reclaimed_mi_b** | **float** |  | [optional] 
**reserved_mi_b** | **float** |  | [optional] 
**total_mi_b** | **float** |  | [optional] 
**used_mi_b** | **float** |  | [optional] 

## Example

```python
from dscc.models.device_type4space import DeviceType4space

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4space from a JSON string
device_type4space_instance = DeviceType4space.from_json(json)
# print the JSON string representation of the object
print(DeviceType4space.to_json())

# convert the object into a dict
device_type4space_dict = device_type4space_instance.to_dict()
# create an instance of DeviceType4space from a dict
device_type4space_from_dict = DeviceType4space.from_dict(device_type4space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


