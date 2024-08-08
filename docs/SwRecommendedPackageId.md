# SwRecommendedPackageId

wip

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayname** | **str** | Display name | [optional] 
**name** | **str** | Name of the resource | [optional] 
**severity** | **str** | Severity. Possible Values: Unknown, CRITICAL, RECOMMENDED, OPTIONAL, AVAILABLE, BLOCKED. | [optional] 
**support_type** | **str** |  | [optional] 

## Example

```python
from dscc.models.sw_recommended_package_id import SwRecommendedPackageId

# TODO update the JSON string below
json = "{}"
# create an instance of SwRecommendedPackageId from a JSON string
sw_recommended_package_id_instance = SwRecommendedPackageId.from_json(json)
# print the JSON string representation of the object
print(SwRecommendedPackageId.to_json())

# convert the object into a dict
sw_recommended_package_id_dict = sw_recommended_package_id_instance.to_dict()
# create an instance of SwRecommendedPackageId from a dict
sw_recommended_package_id_from_dict = SwRecommendedPackageId.from_dict(sw_recommended_package_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


