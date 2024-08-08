# HostState

Host State

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detailed** | [**DeviceType4HostStateDetailed**](DeviceType4HostStateDetailed.md) |  | [optional] 
**overall_state** | **str** | Host State    | [optional] 

## Example

```python
from dscc.models.host_state import HostState

# TODO update the JSON string below
json = "{}"
# create an instance of HostState from a JSON string
host_state_instance = HostState.from_json(json)
# print the JSON string representation of the object
print(HostState.to_json())

# convert the object into a dict
host_state_dict = host_state_instance.to_dict()
# create an instance of HostState from a dict
host_state_from_dict = HostState.from_dict(host_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


