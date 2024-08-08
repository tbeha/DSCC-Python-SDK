# Recommendation

Reccomendations for the device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**check_time** | [**CalendarTime**](CalendarTime.md) |  | [optional] 
**displayname** | **str** | Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**id** | **str** | SystemWWN/UUID string uniquely identifying the object. | [optional] 
**patches** | [**List[SwRecommendedPackageId]**](SwRecommendedPackageId.md) |  | [optional] 
**releases** | [**List[SwRecommendedPackageId]**](SwRecommendedPackageId.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**resource_uri** | **str** | resourceUri for detailed storage object | [optional] 
**system_id** | **str** | SystemUid/serialNumber of the array. | [optional] 
**update_time** | [**CalendarTime**](CalendarTime.md) |  | [optional] 

## Example

```python
from dscc.models.recommendation import Recommendation

# TODO update the JSON string below
json = "{}"
# create an instance of Recommendation from a JSON string
recommendation_instance = Recommendation.from_json(json)
# print the JSON string representation of the object
print(Recommendation.to_json())

# convert the object into a dict
recommendation_dict = recommendation_instance.to_dict()
# create an instance of Recommendation from a dict
recommendation_from_dict = Recommendation.from_dict(recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


