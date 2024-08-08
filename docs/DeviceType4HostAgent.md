# DeviceType4HostAgent

HPE Alletra Storage MP Host Agent

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
**last_updated** | [**DeviceType4HostAgentLastUpdated**](DeviceType4HostAgentLastUpdated.md) |  | [optional] 
**multi_path_software** | **str** | Multipath Software | [optional] 
**multi_path_software_version** | **str** | MultiPath Software Version | [optional] 
**os** | **str** | Operating System Name | [optional] 
**os_patch** | **str** | Os patch | [optional] 
**os_version** | **str** | Os version | [optional] 
**reported_name** | **str** | Reported Name | [optional] 

## Example

```python
from dscc.models.device_type4_host_agent import DeviceType4HostAgent

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4HostAgent from a JSON string
device_type4_host_agent_instance = DeviceType4HostAgent.from_json(json)
# print the JSON string representation of the object
print(DeviceType4HostAgent.to_json())

# convert the object into a dict
device_type4_host_agent_dict = device_type4_host_agent_instance.to_dict()
# create an instance of DeviceType4HostAgent from a dict
device_type4_host_agent_from_dict = DeviceType4HostAgent.from_dict(device_type4_host_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


