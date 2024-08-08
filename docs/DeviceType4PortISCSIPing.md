# DeviceType4PortISCSIPing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IP Address to ping | [optional] 
**ip_addressv6** | **str** | IP Address to ping | [optional] 
**ping_count** | **int** | ping count | [optional] 
**vlan_id** | **str** | VLAN ID | [optional] 

## Example

```python
from dscc.models.device_type4_port_iscsi_ping import DeviceType4PortISCSIPing

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4PortISCSIPing from a JSON string
device_type4_port_iscsi_ping_instance = DeviceType4PortISCSIPing.from_json(json)
# print the JSON string representation of the object
print(DeviceType4PortISCSIPing.to_json())

# convert the object into a dict
device_type4_port_iscsi_ping_dict = device_type4_port_iscsi_ping_instance.to_dict()
# create an instance of DeviceType4PortISCSIPing from a dict
device_type4_port_iscsi_ping_from_dict = DeviceType4PortISCSIPing.from_dict(device_type4_port_iscsi_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


