# DeviceType4softwareVersionsComponentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_version** | **str** | Base Version | [optional] 
**full_version** | **str** | Full Version | [optional] 
**name** | **str** | Name of the Component | [optional] 
**release** | **str** | Release Version | [optional] 
**show_level** | **int** | Show Level | [optional] 

## Example

```python
from dscc.models.device_type4software_versions_components_inner import DeviceType4softwareVersionsComponentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4softwareVersionsComponentsInner from a JSON string
device_type4software_versions_components_inner_instance = DeviceType4softwareVersionsComponentsInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4softwareVersionsComponentsInner.to_json())

# convert the object into a dict
device_type4software_versions_components_inner_dict = device_type4software_versions_components_inner_instance.to_dict()
# create an instance of DeviceType4softwareVersionsComponentsInner from a dict
device_type4software_versions_components_inner_from_dict = DeviceType4softwareVersionsComponentsInner.from_dict(device_type4software_versions_components_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


