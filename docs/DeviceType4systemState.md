# DeviceType4systemState

State of the resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detailed** | **List[Optional[str]]** | Array of the detailed states of the resource | [optional] 
**overall** | **str** | Overall state of the resource | [optional] 

## Example

```python
from dscc.models.device_type4system_state import DeviceType4systemState

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4systemState from a JSON string
device_type4system_state_instance = DeviceType4systemState.from_json(json)
# print the JSON string representation of the object
print(DeviceType4systemState.to_json())

# convert the object into a dict
device_type4system_state_dict = device_type4system_state_instance.to_dict()
# create an instance of DeviceType4systemState from a dict
device_type4system_state_from_dict = DeviceType4systemState.from_dict(device_type4system_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


