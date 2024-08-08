# DeviceType4softwareVersions

Software versions of the product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_version** | **str** | Base Version &#x60;Filter&#x60; | [optional] 
**components** | [**List[DeviceType4softwareVersionsComponentsInner]**](DeviceType4softwareVersionsComponentsInner.md) |  | [optional] 
**full_version** | **str** | Full Version | [optional] 
**patches** | **str** | Set of Patches &#x60;Filter&#x60; | [optional] 
**release** | **str** | Release Version | [optional] 

## Example

```python
from dscc.models.device_type4software_versions import DeviceType4softwareVersions

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4softwareVersions from a JSON string
device_type4software_versions_instance = DeviceType4softwareVersions.from_json(json)
# print the JSON string representation of the object
print(DeviceType4softwareVersions.to_json())

# convert the object into a dict
device_type4software_versions_dict = device_type4software_versions_instance.to_dict()
# create an instance of DeviceType4softwareVersions from a dict
device_type4software_versions_from_dict = DeviceType4softwareVersions.from_dict(device_type4software_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


