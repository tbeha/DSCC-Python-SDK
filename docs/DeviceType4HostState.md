# DeviceType4HostState

Host State

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detailed** | [**DeviceType4HostStateDetailed**](DeviceType4HostStateDetailed.md) |  | [optional] 
**overall** | **str** | Host State    | [optional] 

## Example

```python
from dscc.models.device_type4_host_state import DeviceType4HostState

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostState from a JSON string
device_type4_host_state_instance = DeviceType4HostState.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostState.to_json())

# convert the object into a dict
device_type4_host_state_dict = device_type4_host_state_instance.to_dict()
# create an instance of DeviceType4HostState from a dict
device_type4_host_state_from_dict = DeviceType4HostState.from_dict(device_type4_host_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


