# LicenseFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration** | [**DeviceType4Calendar**](DeviceType4Calendar.md) |  | [optional] 
**name** | **str** | The name of the licensed feature | [optional] 
**size_or_count** | **str** | The size (capacity) or the count of objects allowed by the feature | [optional] 

## Example

```python
from dscc.models.license_feature import LicenseFeature

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseFeature from a JSON string
license_feature_instance = LicenseFeature.from_json(json)
# print the JSON string representation of the object
print(LicenseFeature.to_json())

# convert the object into a dict
license_feature_dict = license_feature_instance.to_dict()
# create an instance of LicenseFeature from a dict
license_feature_from_dict = LicenseFeature.from_dict(license_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


