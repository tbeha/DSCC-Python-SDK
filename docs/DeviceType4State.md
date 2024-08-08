# DeviceType4State

State of the resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detailed** | **List[Optional[str]]** | Array of the detailed states of the resource | [optional] 
**overall** | **str** | Overall state of the resource | [optional] 

## Example

```python
from dscc.models.device_type4_state import DeviceType4State

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4State from a JSON string
device_type4_state_instance = DeviceType4State.from_json(json)
# print the JSON string representation of the object
print(DeviceType4State.to_json())

# convert the object into a dict
device_type4_state_dict = device_type4_state_instance.to_dict()
# create an instance of DeviceType4State from a dict
device_type4_state_from_dict = DeviceType4State.from_dict(device_type4_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


