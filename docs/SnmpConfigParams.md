# SnmpConfigParams


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
from dscc.models.snmp_config_params import SnmpConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpConfigParams from a JSON string
snmp_config_params_instance = SnmpConfigParams.from_json(json)
# print the JSON string representation of the object
print(SnmpConfigParams.to_json())

# convert the object into a dict
snmp_config_params_dict = snmp_config_params_instance.to_dict()
# create an instance of SnmpConfigParams from a dict
snmp_config_params_from_dict = SnmpConfigParams.from_dict(snmp_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


