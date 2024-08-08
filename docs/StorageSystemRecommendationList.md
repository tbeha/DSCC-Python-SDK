# StorageSystemRecommendationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RecommendationList]**](RecommendationList.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**total** | **int** | Number of systems | [optional] 

## Example

```python
from dscc.models.storage_system_recommendation_list import StorageSystemRecommendationList

# TODO update the JSON string below
json = "{}"
# create an instance of StorageSystemRecommendationList from a JSON string
storage_system_recommendation_list_instance = StorageSystemRecommendationList.from_json(json)
# print the JSON string representation of the object
print(StorageSystemRecommendationList.to_json())

# convert the object into a dict
storage_system_recommendation_list_dict = storage_system_recommendation_list_instance.to_dict()
# create an instance of StorageSystemRecommendationList from a dict
storage_system_recommendation_list_from_dict = StorageSystemRecommendationList.from_dict(storage_system_recommendation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


