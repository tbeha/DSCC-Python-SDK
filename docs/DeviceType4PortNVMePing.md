# DeviceType4PortNVMePing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packet_size** | **int** | Packet size for the NVMe ping operation | [optional] 
**wait_time** | **int** | Wait time for the NVMe ping operation | [optional] 
**ip_address** | **str** | IP address of NVMe port | [optional] 
**ip_addressv6** | **str** | IP address of NVMe port | [optional] 
**ping_count** | **int** | Count for the NVMe ping operation | [optional] 

## Example

```python
from dscc.models.device_type4_port_nvme_ping import DeviceType4PortNVMePing

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortNVMePing from a JSON string
device_type4_port_nvme_ping_instance = DeviceType4PortNVMePing.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortNVMePing.to_json())

# convert the object into a dict
device_type4_port_nvme_ping_dict = device_type4_port_nvme_ping_instance.to_dict()
# create an instance of DeviceType4PortNVMePing from a dict
device_type4_port_nvme_ping_from_dict = DeviceType4PortNVMePing.from_dict(device_type4_port_nvme_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


