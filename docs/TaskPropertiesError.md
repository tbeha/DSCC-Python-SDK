# TaskPropertiesError

The error response status of the operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | A user friendly error message | 
**error_code** | **str** | A machine-friendly identifier for the error response | 
**trace_id** | **str** | A unique identifier for the request | 

## Example

```python
from dscc.models.task_properties_error import TaskPropertiesError

# TODO update the JSON string below
json = "{}"
# create an instance of TaskPropertiesError from a JSON string
task_properties_error_instance = TaskPropertiesError.from_json(json)
# print the JSON string representation of the object
print(TaskPropertiesError.to_json())

# convert the object into a dict
task_properties_error_dict = task_properties_error_instance.to_dict()
# create an instance of TaskPropertiesError from a dict
task_properties_error_from_dict = TaskPropertiesError.from_dict(task_properties_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


