# TasksForbidden


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **object** | Possible values: FORBIDDEN | [optional] 
**error** | **str** | A user friendly error message | 
**trace_id** | **str** | A unique identifier for the request | 

## Example

```python
from dscc.models.tasks_forbidden import TasksForbidden

# TODO update the JSON string below
json = "{}"
# create an instance of TasksForbidden from a JSON string
tasks_forbidden_instance = TasksForbidden.from_json(json)
# print the JSON string representation of the object
print(TasksForbidden.to_json())

# convert the object into a dict
tasks_forbidden_dict = tasks_forbidden_instance.to_dict()
# create an instance of TasksForbidden from a dict
tasks_forbidden_from_dict = TasksForbidden.from_dict(tasks_forbidden_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


