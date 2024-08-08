# Version


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** | Base version | [optional] 
**display** | **str** | Display name | [optional] 
**full** | **str** | Full version | [optional] 
**full_without_patches** | **str** | Base version without patches | [optional] 

## Example

```python
from dscc.models.version import Version

# TODO update the JSON string below
json = "{}"
# create an instance of Version from a JSON string
version_instance = Version.from_json(json)
# print the JSON string representation of the object
print(Version.to_json())

# convert the object into a dict
version_dict = version_instance.to_dict()
# create an instance of Version from a dict
version_from_dict = Version.from_dict(version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


