# DeviceType4swRecommendedPackageId

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
from dscc.models.device_type4sw_recommended_package_id import DeviceType4swRecommendedPackageId

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4swRecommendedPackageId from a JSON string
device_type4sw_recommended_package_id_instance = DeviceType4swRecommendedPackageId.from_json(json)
# print the JSON string representation of the object
print(DeviceType4swRecommendedPackageId.to_json())

# convert the object into a dict
device_type4sw_recommended_package_id_dict = device_type4sw_recommended_package_id_instance.to_dict()
# create an instance of DeviceType4swRecommendedPackageId from a dict
device_type4sw_recommended_package_id_from_dict = DeviceType4swRecommendedPackageId.from_dict(device_type4sw_recommended_package_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


