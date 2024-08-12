# TaskPropertiesParentTask

The parent is the task that initiated this sub-task. If this is not a sub-task this will be a self reference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**resource_uri** | **str** |  | [readonly] 
**type** | **str** |  | [readonly] 

## Example

```python
from dscc.models.task_properties_parent_task import TaskPropertiesParentTask

# TODO update the JSON string below
json = "{}"
# create an instance of TaskPropertiesParentTask from a JSON string
task_properties_parent_task_instance = TaskPropertiesParentTask.from_json(json)
# print the JSON string representation of the object
print(TaskPropertiesParentTask.to_json())

# convert the object into a dict
task_properties_parent_task_dict = task_properties_parent_task_instance.to_dict()
# create an instance of TaskPropertiesParentTask from a dict
task_properties_parent_task_from_dict = TaskPropertiesParentTask.from_dict(task_properties_parent_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


