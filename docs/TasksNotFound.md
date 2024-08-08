# TasksNotFound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **object** | Possible values: NOT_FOUND | [optional] 
**error** | **str** | A user friendly error message | 
**trace_id** | **str** | A unique identifier for the request | 

## Example

```python
from dscc.models.tasks_not_found import TasksNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of TasksNotFound from a JSON string
tasks_not_found_instance = TasksNotFound.from_json(json)
# print the JSON string representation of the object
print(TasksNotFound.to_json())

# convert the object into a dict
tasks_not_found_dict = tasks_not_found_instance.to_dict()
# create an instance of TasksNotFound from a dict
tasks_not_found_from_dict = TasksNotFound.from_dict(tasks_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


