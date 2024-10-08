# NwSnmpMgrEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manager_ip** | **str** | Specify the IP address of the host from which the manager runs | [optional] 
**notify** | **str** | Indicates the trap notification types defined by the HPE deviceType1 MIB | [optional] 
**port** | **int** | Specify the port number where the SNMP manager receives traps | [optional] 
**retry** | **int** | Specify the number of times to send a trap (retry) if the SNMP manager is not available. | [optional] 
**timeout_secs** | **int** | Specify the number of seconds to wait before sending a trap (timeout). | [optional] 
**user** | **str** | Specify the SNMPv3 user name | [optional] 
**version** | **int** | Specify the SNMP version supported | [optional] 

## Example

```python
from dscc.models.nw_snmp_mgr_edit import NwSnmpMgrEdit

# TODO update the JSON string below
json = "{}"
# create an instance of NwSnmpMgrEdit from a JSON string
nw_snmp_mgr_edit_instance = NwSnmpMgrEdit.from_json(json)
# print the JSON string representation of the object
print(NwSnmpMgrEdit.to_json())

# convert the object into a dict
nw_snmp_mgr_edit_dict = nw_snmp_mgr_edit_instance.to_dict()
# create an instance of NwSnmpMgrEdit from a dict
nw_snmp_mgr_edit_from_dict = NwSnmpMgrEdit.from_dict(nw_snmp_mgr_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


