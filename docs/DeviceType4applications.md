# DeviceType4applications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_set_type** | **str** | Name of the application | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**total_size_mi_b** | **float** | The total volume size in MiB of the application | [optional] 
**total_used_size_mi_b** | **float** | The total used size in Mib of the application | [optional] 
**volumes_count** | **int** | The number of volumes in an application | [optional] 

## Example

```python
from dscc.models.device_type4applications import DeviceType4applications

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4applications from a JSON string
device_type4applications_instance = DeviceType4applications.from_json(json)
# print the JSON string representation of the object
print(DeviceType4applications.to_json())

# convert the object into a dict
device_type4applications_dict = device_type4applications_instance.to_dict()
# create an instance of DeviceType4applications from a dict
device_type4applications_from_dict = DeviceType4applications.from_dict(device_type4applications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


