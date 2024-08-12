# HostAgentLastUpdated

Primera Host Agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch Time | [optional] 
**tz** | **str** | String Time | [optional] 

## Example

```python
from dscc.models.host_agent_last_updated import HostAgentLastUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of HostAgentLastUpdated from a JSON string
host_agent_last_updated_instance = HostAgentLastUpdated.from_json(json)
# print the JSON string representation of the object
print(HostAgentLastUpdated.to_json())

# convert the object into a dict
host_agent_last_updated_dict = host_agent_last_updated_instance.to_dict()
# create an instance of HostAgentLastUpdated from a dict
host_agent_last_updated_from_dict = HostAgentLastUpdated.from_dict(host_agent_last_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


