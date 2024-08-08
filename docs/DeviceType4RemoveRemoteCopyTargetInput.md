# DeviceType4RemoveRemoteCopyTargetInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partner_system_id** | **str** | SystemId of target replication partner | [optional] 
**src_replication_id** | **str** | Id of source replication partner | 
**target_replication_id** | **str** | Id of target replication partner | [optional] 

## Example

```python
from dscc.models.device_type4_remove_remote_copy_target_input import DeviceType4RemoveRemoteCopyTargetInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RemoveRemoteCopyTargetInput from a JSON string
device_type4_remove_remote_copy_target_input_instance = DeviceType4RemoveRemoteCopyTargetInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RemoveRemoteCopyTargetInput.to_json())

# convert the object into a dict
device_type4_remove_remote_copy_target_input_dict = device_type4_remove_remote_copy_target_input_instance.to_dict()
# create an instance of DeviceType4RemoveRemoteCopyTargetInput from a dict
device_type4_remove_remote_copy_target_input_from_dict = DeviceType4RemoveRemoteCopyTargetInput.from_dict(device_type4_remove_remote_copy_target_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


