# SoftwareVersionsComponentsInner


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
from dscc.models.software_versions_components_inner import SoftwareVersionsComponentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareVersionsComponentsInner from a JSON string
software_versions_components_inner_instance = SoftwareVersionsComponentsInner.from_json(json)
# print the JSON string representation of the object
print(SoftwareVersionsComponentsInner.to_json())

# convert the object into a dict
software_versions_components_inner_dict = software_versions_components_inner_instance.to_dict()
# create an instance of SoftwareVersionsComponentsInner from a dict
software_versions_components_inner_from_dict = SoftwareVersionsComponentsInner.from_dict(software_versions_components_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


