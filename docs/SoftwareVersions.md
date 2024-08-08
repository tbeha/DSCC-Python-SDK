# SoftwareVersions

Software versions of the product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_version** | **str** | Base Version &#x60;Filter&#x60; | [optional] 
**components** | [**List[SoftwareVersionsComponentsInner]**](SoftwareVersionsComponentsInner.md) |  | [optional] 
**full_version** | **str** | Full Version | [optional] 
**patches** | **str** | Set of Patches &#x60;Filter&#x60; | [optional] 
**release** | **str** | Release Version | [optional] 

## Example

```python
from dscc.models.software_versions import SoftwareVersions

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareVersions from a JSON string
software_versions_instance = SoftwareVersions.from_json(json)
# print the JSON string representation of the object
print(SoftwareVersions.to_json())

# convert the object into a dict
software_versions_dict = software_versions_instance.to_dict()
# create an instance of SoftwareVersions from a dict
software_versions_from_dict = SoftwareVersions.from_dict(software_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


