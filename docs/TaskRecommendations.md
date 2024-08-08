# TaskRecommendations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from dscc.models.task_recommendations import TaskRecommendations

# TODO update the JSON string below
json = "{}"
# create an instance of TaskRecommendations from a JSON string
task_recommendations_instance = TaskRecommendations.from_json(json)
# print the JSON string representation of the object
print(TaskRecommendations.to_json())

# convert the object into a dict
task_recommendations_dict = task_recommendations_instance.to_dict()
# create an instance of TaskRecommendations from a dict
task_recommendations_from_dict = TaskRecommendations.from_dict(task_recommendations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


