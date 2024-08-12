# TaskResponseReplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[NimbleTestConfigurationResponse]**](NimbleTestConfigurationResponse.md) | Test Configuration Response. | [optional] 

## Example

```python
from dscc.models.task_response_replication import TaskResponseReplication

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResponseReplication from a JSON string
task_response_replication_instance = TaskResponseReplication.from_json(json)
# print the JSON string representation of the object
print(TaskResponseReplication.to_json())

# convert the object into a dict
task_response_replication_dict = task_response_replication_instance.to_dict()
# create an instance of TaskResponseReplication from a dict
task_response_replication_from_dict = TaskResponseReplication.from_dict(task_response_replication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


