# TaskConsoleReference

References to other UI link include the consoleUri

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**console_uri** | **str** |  | 

## Example

```python
from dscc.models.task_console_reference import TaskConsoleReference

# TODO update the JSON string below
json = "{}"
# create an instance of TaskConsoleReference from a JSON string
task_console_reference_instance = TaskConsoleReference.from_json(json)
# print the JSON string representation of the object
print(TaskConsoleReference.to_json())

# convert the object into a dict
task_console_reference_dict = task_console_reference_instance.to_dict()
# create an instance of TaskConsoleReference from a dict
task_console_reference_from_dict = TaskConsoleReference.from_dict(task_console_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


