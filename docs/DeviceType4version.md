# DeviceType4version


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** | Base version | [optional] 
**display** | **str** | Display name | [optional] 
**full** | **str** | Full version | [optional] 
**full_without_patches** | **str** | Base version without patches | [optional] 

## Example

```python
from dscc.models.device_type4version import DeviceType4version

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4version from a JSON string
device_type4version_instance = DeviceType4version.from_json(json)
# print the JSON string representation of the object
print(DeviceType4version.to_json())

# convert the object into a dict
device_type4version_dict = device_type4version_instance.to_dict()
# create an instance of DeviceType4version from a dict
device_type4version_from_dict = DeviceType4version.from_dict(device_type4version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


