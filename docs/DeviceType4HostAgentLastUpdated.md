# DeviceType4HostAgentLastUpdated

HPE Alletra Storage MP Host Agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch Time | [optional] 
**tz** | **str** | String Time | [optional] 

## Example

```python
from dscc.models.device_type4_host_agent_last_updated import DeviceType4HostAgentLastUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostAgentLastUpdated from a JSON string
device_type4_host_agent_last_updated_instance = DeviceType4HostAgentLastUpdated.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostAgentLastUpdated.to_json())

# convert the object into a dict
device_type4_host_agent_last_updated_dict = device_type4_host_agent_last_updated_instance.to_dict()
# create an instance of DeviceType4HostAgentLastUpdated from a dict
device_type4_host_agent_last_updated_from_dict = DeviceType4HostAgentLastUpdated.from_dict(device_type4_host_agent_last_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


