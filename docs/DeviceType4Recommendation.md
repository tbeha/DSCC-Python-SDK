# DeviceType4Recommendation

Reccomendations for the device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**check_time** | [**DeviceType4calendarTime**](DeviceType4calendarTime.md) |  | [optional] 
**displayname** | **str** | Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**id** | **str** | SystemWWN/UUID string uniquely identifying the object. | [optional] 
**patches** | [**List[DeviceType4swRecommendedPackageId]**](DeviceType4swRecommendedPackageId.md) |  | [optional] 
**releases** | [**List[DeviceType4swRecommendedPackageId]**](DeviceType4swRecommendedPackageId.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**resource_uri** | **str** | resourceUri for detailed storage object | [optional] 
**system_id** | **str** | SystemUid/serialNumber of the array. | [optional] 
**update_time** | [**DeviceType4calendarTime**](DeviceType4calendarTime.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_recommendation import DeviceType4Recommendation

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4Recommendation from a JSON string
device_type4_recommendation_instance = DeviceType4Recommendation.from_json(json)
# print the JSON string representation of the object
print(DeviceType4Recommendation.to_json())

# convert the object into a dict
device_type4_recommendation_dict = device_type4_recommendation_instance.to_dict()
# create an instance of DeviceType4Recommendation from a dict
device_type4_recommendation_from_dict = DeviceType4Recommendation.from_dict(device_type4_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


