# SoftwareVersionsSolo

Software versions of the product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_version** | **str** | Base Version | [optional] 
**components** | [**List[DeviceType4softwareVersionsSoloComponentsInner]**](DeviceType4softwareVersionsSoloComponentsInner.md) |  | [optional] 
**full_version** | **str** | Full Version | [optional] 
**patches** | **str** | Set of Patches | [optional] 
**release** | **str** | Release Version | [optional] 

## Example

```python
from dscc.models.software_versions_solo import SoftwareVersionsSolo

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareVersionsSolo from a JSON string
software_versions_solo_instance = SoftwareVersionsSolo.from_json(json)
# print the JSON string representation of the object
print(SoftwareVersionsSolo.to_json())

# convert the object into a dict
software_versions_solo_dict = software_versions_solo_instance.to_dict()
# create an instance of SoftwareVersionsSolo from a dict
software_versions_solo_from_dict = SoftwareVersionsSolo.from_dict(software_versions_solo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


