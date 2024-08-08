# RemoveRemoteCopyTargetInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partner_system_id** | **str** | SystemId of target replication partner | [optional] 
**src_replication_id** | **str** | Id of source replication partner | 
**target_replication_id** | **str** | Id of target replication partner | [optional] 

## Example

```python
from dscc.models.remove_remote_copy_target_input import RemoveRemoteCopyTargetInput

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveRemoteCopyTargetInput from a JSON string
remove_remote_copy_target_input_instance = RemoveRemoteCopyTargetInput.from_json(json)
# print the JSON string representation of the object
print(RemoveRemoteCopyTargetInput.to_json())

# convert the object into a dict
remove_remote_copy_target_input_dict = remove_remote_copy_target_input_instance.to_dict()
# create an instance of RemoveRemoteCopyTargetInput from a dict
remove_remote_copy_target_input_from_dict = RemoveRemoteCopyTargetInput.from_dict(remove_remote_copy_target_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


