# DeviceType4NwSnmpMgrEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_password** | **str** | Specify the SNMPv3 Authentication Password | [optional] 
**manager_ip** | **str** | Specify the IP address of the host from which the manager runs | [optional] 
**notify** | **str** | Indicates the trap notification types defined by the HPE deviceType1 MIB | [optional] 
**port** | **int** | Specify the port number where the SNMP manager receives traps | [optional] 
**priv_password** | **str** | Specify the SNMPv3 Authentication Password | [optional] 
**retry** | **int** | Specify the number of times to send a trap (retry) if the SNMP manager is not available. | [optional] 
**timeout_secs** | **int** | Specify the number of seconds to wait before sending a trap (timeout). | [optional] 
**user** | **str** | Specify the SNMPv3 user name | [optional] 
**user_mode** | **str** | Specify the SNMPv3 user mode | [optional] 
**version** | **int** | Specify the SNMP version supported | [optional] 

## Example

```python
from dscc.models.device_type4_nw_snmp_mgr_edit import DeviceType4NwSnmpMgrEdit

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4NwSnmpMgrEdit from a JSON string
device_type4_nw_snmp_mgr_edit_instance = DeviceType4NwSnmpMgrEdit.from_json(json)
# print the JSON string representation of the object
print(DeviceType4NwSnmpMgrEdit.to_json())

# convert the object into a dict
device_type4_nw_snmp_mgr_edit_dict = device_type4_nw_snmp_mgr_edit_instance.to_dict()
# create an instance of DeviceType4NwSnmpMgrEdit from a dict
device_type4_nw_snmp_mgr_edit_from_dict = DeviceType4NwSnmpMgrEdit.from_dict(device_type4_nw_snmp_mgr_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


