# Task

The task resource provides information about progress of asynchronous request processing and is where associated resources can be found. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | The customer application identifier | [optional] [readonly] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] [readonly] 
**id** | **str** | An identifier for the resource, usually a UUID. | [optional] [readonly] 
**name** | **str** | A system specified name for the resource. | [optional] 
**resource_uri** | **str** | The &#39;self&#39; reference for this resource. | [optional] [readonly] 
**type** | **str** | The type of resource. | [optional] [readonly] 
**additional_details** | [**TaskConsoleReference**](TaskConsoleReference.md) | A link to be displayed in the Tasks UI. This can be used when a task is paused to take the user to the console UI page with information on how to unpause the task, or for more general information when the task is in other states. | [optional] 
**associated_resources** | [**List[ResourceReference]**](ResourceReference.md) | Resources that are associated with the task. These may be created by the task or other resources that are involved in the task. | [optional] 
**child_tasks** | [**List[ResourceReference]**](ResourceReference.md) | A list of sub-tasks that were initiated by this task. | [optional] 
**created_at** | **datetime** | The time this task was created. | [optional] 
**display_name** | **str** | The displayed name for the task. | [optional] 
**ended_at** | **datetime** | The time this task completed. | [optional] 
**error** | [**TaskPropertiesError**](TaskPropertiesError.md) |  | [optional] 
**estimated_running_duration_minutes** | **int** | An estimate of how long the task will run before completing. | [optional] 
**health_status** | **str** | The health status indicates if any errors or problems have been encountered during the processing of the task.  Expected values are OK, ERROR, WARNING, UNKNOWN, and UNSPECIFIED.  | [optional] 
**log_messages** | [**List[TaskLogMessage]**](TaskLogMessage.md) | Time stamped messages that record the progress of the task. | [optional] 
**parent_task** | [**TaskPropertiesParentTask**](TaskPropertiesParentTask.md) |  | [optional] 
**progress_percent** | **int** | A percentage representation of progress to completion. | [optional] 
**recommendations** | [**List[TaskRecommendations]**](TaskRecommendations.md) | Recommendations on how to fix failing tasks. | [optional] 
**source_resource** | [**TaskPropertiesSourceResource**](TaskPropertiesSourceResource.md) |  | [optional] 
**started_at** | **datetime** | The time this task was started. | [optional] 
**state** | **str** | A message to indicate the current state of the task, for example the current step in a workflow. Expected values are INITIALIZED, RUNNING, FAILED, SUCCEEDED, TIMEDOUT, PAUSED, and UNSPECIFIED.  | [optional] 
**suggested_polling_interval_seconds** | **int** | This attribute suggests a suitable interval to use when polling for progress. Where specified this will be based on the frequency with which the task is likely to be updated. | [optional] 
**updated_at** | **datetime** | The time this task was last updated. | [optional] 
**user_id** | **str** | The ID or email address of the user that initiated the task. | [optional] 

## Example

```python
from dscc.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


