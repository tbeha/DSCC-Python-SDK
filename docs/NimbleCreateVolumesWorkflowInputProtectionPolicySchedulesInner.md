# NimbleCreateVolumesWorkflowInputProtectionPolicySchedulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock_period** | **int** | Number of seconds to keep a snapshot as immutable. | [optional] 
**name** | **str** | Name | [optional] 
**start_time** | **str** | start time | [optional] 

## Example

```python
from dscc.models.nimble_create_volumes_workflow_input_protection_policy_schedules_inner import NimbleCreateVolumesWorkflowInputProtectionPolicySchedulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleCreateVolumesWorkflowInputProtectionPolicySchedulesInner from a JSON string
nimble_create_volumes_workflow_input_protection_policy_schedules_inner_instance = NimbleCreateVolumesWorkflowInputProtectionPolicySchedulesInner.from_json(json)
# print the JSON string representation of the object
print(NimbleCreateVolumesWorkflowInputProtectionPolicySchedulesInner.to_json())

# convert the object into a dict
nimble_create_volumes_workflow_input_protection_policy_schedules_inner_dict = nimble_create_volumes_workflow_input_protection_policy_schedules_inner_instance.to_dict()
# create an instance of NimbleCreateVolumesWorkflowInputProtectionPolicySchedulesInner from a dict
nimble_create_volumes_workflow_input_protection_policy_schedules_inner_from_dict = NimbleCreateVolumesWorkflowInputProtectionPolicySchedulesInner.from_dict(nimble_create_volumes_workflow_input_protection_policy_schedules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


