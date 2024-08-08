# DeviceType4SwitchOverParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_snapshot** | **bool** | Specifies that snapshots are not taken of application sets that are switched from secondary to primary. Additionally, existing snapshots are deleted if application sets are switched from primary to secondary. The use of this option may result in a full synchronization of the secondary volumes. | [optional] 
**target_name** | **str** | Replication partner name (target name) on which the switchover action is to be performed. | [optional] 

## Example

```python
from dscc.models.device_type4_switch_over_params import DeviceType4SwitchOverParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SwitchOverParams from a JSON string
device_type4_switch_over_params_instance = DeviceType4SwitchOverParams.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SwitchOverParams.to_json())

# convert the object into a dict
device_type4_switch_over_params_dict = device_type4_switch_over_params_instance.to_dict()
# create an instance of DeviceType4SwitchOverParams from a dict
device_type4_switch_over_params_from_dict = DeviceType4SwitchOverParams.from_dict(device_type4_switch_over_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


