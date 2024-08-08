# SwitchOverParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_name** | **str** | Replication partner name (target name) on which the switchover action is to be performed. | [optional] 

## Example

```python
from dscc.models.switch_over_params import SwitchOverParams

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchOverParams from a JSON string
switch_over_params_instance = SwitchOverParams.from_json(json)
# print the JSON string representation of the object
print(SwitchOverParams.to_json())

# convert the object into a dict
switch_over_params_dict = switch_over_params_instance.to_dict()
# create an instance of SwitchOverParams from a dict
switch_over_params_from_dict = SwitchOverParams.from_dict(switch_over_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


