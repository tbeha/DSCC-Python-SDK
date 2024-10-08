# DeviceType4snmp

SNMP manager details for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**id** | **str** | Unique Identifier of the resource | [optional] 
**manager_ip** | **str** | Specify the IP address of the host from which the manager runs | [optional] 
**notify** | **str** | Indicates the trap notification types defined by the HPE deviceType1 MIB | [optional] 
**port** | **int** | Specify the port number where the SNMP manager receives traps | [optional] 
**system_id** | **str** | SystemId of the storage system | [optional] 
**system_wwn** | **str** | WWN of the array | [optional] 
**type** | **str** | The type of resource. | [optional] 
**user** | **str** | Specify the SNMPv3 user name | [optional] 
**version** | **int** | Specify the SNMP version supported | [optional] 

## Example

```python
from dscc.models.device_type4snmp import DeviceType4snmp

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4snmp from a JSON string
device_type4snmp_instance = DeviceType4snmp.from_json(json)
# print the JSON string representation of the object
print(DeviceType4snmp.to_json())

# convert the object into a dict
device_type4snmp_dict = device_type4snmp_instance.to_dict()
# create an instance of DeviceType4snmp from a dict
device_type4snmp_from_dict = DeviceType4snmp.from_dict(device_type4snmp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


