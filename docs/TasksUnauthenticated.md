# TasksUnauthenticated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **object** | Possible values: UNAUTHENTICATED | [optional] 
**error** | **str** | A user friendly error message | 
**trace_id** | **str** | A unique identifier for the request | 

## Example

```python
from dscc.models.tasks_unauthenticated import TasksUnauthenticated

# TODO update the JSON string below
json = "{}"
# create an instance of TasksUnauthenticated from a JSON string
tasks_unauthenticated_instance = TasksUnauthenticated.from_json(json)
# print the JSON string representation of the object
print(TasksUnauthenticated.to_json())

# convert the object into a dict
tasks_unauthenticated_dict = tasks_unauthenticated_instance.to_dict()
# create an instance of TasksUnauthenticated from a dict
tasks_unauthenticated_from_dict = TasksUnauthenticated.from_dict(tasks_unauthenticated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


