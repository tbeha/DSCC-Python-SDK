# TaskLogMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**timestamp_at** | **datetime** |  | 

## Example

```python
from dscc.models.task_log_message import TaskLogMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TaskLogMessage from a JSON string
task_log_message_instance = TaskLogMessage.from_json(json)
# print the JSON string representation of the object
print(TaskLogMessage.to_json())

# convert the object into a dict
task_log_message_dict = task_log_message_instance.to_dict()
# create an instance of TaskLogMessage from a dict
task_log_message_from_dict = TaskLogMessage.from_dict(task_log_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


