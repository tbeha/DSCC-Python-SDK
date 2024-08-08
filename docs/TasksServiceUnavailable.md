# TasksServiceUnavailable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **object** | Possible values: SERVICE_UNAVAILABLE | [optional] 
**error** | **str** | A user friendly error message | 
**trace_id** | **str** | A unique identifier for the request | 

## Example

```python
from dscc.models.tasks_service_unavailable import TasksServiceUnavailable

# TODO update the JSON string below
json = "{}"
# create an instance of TasksServiceUnavailable from a JSON string
tasks_service_unavailable_instance = TasksServiceUnavailable.from_json(json)
# print the JSON string representation of the object
print(TasksServiceUnavailable.to_json())

# convert the object into a dict
tasks_service_unavailable_dict = tasks_service_unavailable_instance.to_dict()
# create an instance of TasksServiceUnavailable from a dict
tasks_service_unavailable_from_dict = TasksServiceUnavailable.from_dict(tasks_service_unavailable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


