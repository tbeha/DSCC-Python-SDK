# DeviceType4OverrideParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_name** | **str** | Replication partner name (target name) on which the override action is to be performed. | [optional] 

## Example

```python
from dscc.models.device_type4_override_params import DeviceType4OverrideParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4OverrideParams from a JSON string
device_type4_override_params_instance = DeviceType4OverrideParams.from_json(json)
# print the JSON string representation of the object
print(DeviceType4OverrideParams.to_json())

# convert the object into a dict
device_type4_override_params_dict = device_type4_override_params_instance.to_dict()
# create an instance of DeviceType4OverrideParams from a dict
device_type4_override_params_from_dict = DeviceType4OverrideParams.from_dict(device_type4_override_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


