# PortRCIPPing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packet_size** | **int** | Packet size of the ping | [optional] 
**wait_time** | **int** | Wait time | [optional] 
**ip_address** | **str** | IP Address to ping | [optional] 
**ip_addressv6** | **str** | IP Address to ping | [optional] 
**ping_count** | **int** | ping count | [optional] 

## Example

```python
from dscc.models.port_rcip_ping import PortRCIPPing

# TODO update the JSON string below
json = "{}"
# create an instance of PortRCIPPing from a JSON string
port_rcip_ping_instance = PortRCIPPing.from_json(json)
# print the JSON string representation of the object
print(PortRCIPPing.to_json())

# convert the object into a dict
port_rcip_ping_dict = port_rcip_ping_instance.to_dict()
# create an instance of PortRCIPPing from a dict
port_rcip_ping_from_dict = PortRCIPPing.from_dict(port_rcip_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


