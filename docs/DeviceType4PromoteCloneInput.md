# DeviceType4PromoteCloneInput

Promote clone input. Promote a clone volume with given priority.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | [**DeviceType4ClonePriority**](DeviceType4ClonePriority.md) |  | [optional] 

## Example

```python
from dscc.models.device_type4_promote_clone_input import DeviceType4PromoteCloneInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PromoteCloneInput from a JSON string
device_type4_promote_clone_input_instance = DeviceType4PromoteCloneInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PromoteCloneInput.to_json())

# convert the object into a dict
device_type4_promote_clone_input_dict = device_type4_promote_clone_input_instance.to_dict()
# create an instance of DeviceType4PromoteCloneInput from a dict
device_type4_promote_clone_input_from_dict = DeviceType4PromoteCloneInput.from_dict(device_type4_promote_clone_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


