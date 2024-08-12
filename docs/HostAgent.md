# HostAgent

Primera Host Agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_addr** | **str** | Ip Address | [optional] 
**architecture** | **str** | Architecture Name | [optional] 
**boot_from_san** | **str** | Boot from SAN | [optional] 
**cluster_id** | **str** | Cluster ID  | [optional] 
**cluster_name** | **str** | Cluster Cluster | [optional] 
**cluster_software** | **str** | Cluster OS | [optional] 
**cluster_version** | **str** | Cluster Version  | [optional] 
**host_apps** | **str** | Host Applications | [optional] 
**last_updated** | [**HostAgentLastUpdated**](HostAgentLastUpdated.md) |  | [optional] 
**multi_path_software** | **str** | Multipath Software | [optional] 
**multi_path_software_version** | **str** | MultiPath Software Version | [optional] 
**os** | **str** | Operating System Name | [optional] 
**os_patch** | **str** | Os patch | [optional] 
**os_version** | **str** | Os version | [optional] 
**reported_name** | **str** | Reported Name | [optional] 

## Example

```python
from dscc.models.host_agent import HostAgent

# TODO update the JSON string below
json = "{}"
# create an instance of HostAgent from a JSON string
host_agent_instance = HostAgent.from_json(json)
# print the JSON string representation of the object
print(HostAgent.to_json())

# convert the object into a dict
host_agent_dict = host_agent_instance.to_dict()
# create an instance of HostAgent from a dict
host_agent_from_dict = HostAgent.from_dict(host_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


