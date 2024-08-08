# TasksBadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **object** | Possible values: BAD_REQUEST, INVALID_PARAMETER | [optional] 
**error** | **str** | A user friendly error message | 
**trace_id** | **str** | A unique identifier for the request | 

## Example

```python
from dscc.models.tasks_bad_request import TasksBadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TasksBadRequest from a JSON string
tasks_bad_request_instance = TasksBadRequest.from_json(json)
# print the JSON string representation of the object
print(TasksBadRequest.to_json())

# convert the object into a dict
tasks_bad_request_dict = tasks_bad_request_instance.to_dict()
# create an instance of TasksBadRequest from a dict
tasks_bad_request_from_dict = TasksBadRequest.from_dict(tasks_bad_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


