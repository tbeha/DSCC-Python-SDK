# TaskPropertiesSourceResource

The resource that was used to initiate the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**resource_uri** | **str** |  | [readonly] 
**type** | **str** |  | [readonly] 

## Example

```python
from dscc.models.task_properties_source_resource import TaskPropertiesSourceResource

# TODO update the JSON string below
json = "{}"
# create an instance of TaskPropertiesSourceResource from a JSON string
task_properties_source_resource_instance = TaskPropertiesSourceResource.from_json(json)
# print the JSON string representation of the object
print(TaskPropertiesSourceResource.to_json())

# convert the object into a dict
task_properties_source_resource_dict = task_properties_source_resource_instance.to_dict()
# create an instance of TaskPropertiesSourceResource from a dict
task_properties_source_resource_from_dict = TaskPropertiesSourceResource.from_dict(task_properties_source_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


