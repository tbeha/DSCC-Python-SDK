# DeviceType4NwAddSnmpMgr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snmp_config** | [**List[DeviceType4SnmpConfigParams]**](DeviceType4SnmpConfigParams.md) | Specify the SNMP params | [optional] 

## Example

```python
from dscc.models.device_type4_nw_add_snmp_mgr import DeviceType4NwAddSnmpMgr

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4NwAddSnmpMgr from a JSON string
device_type4_nw_add_snmp_mgr_instance = DeviceType4NwAddSnmpMgr.from_json(json)
# print the JSON string representation of the object
print(DeviceType4NwAddSnmpMgr.to_json())

# convert the object into a dict
device_type4_nw_add_snmp_mgr_dict = device_type4_nw_add_snmp_mgr_instance.to_dict()
# create an instance of DeviceType4NwAddSnmpMgr from a dict
device_type4_nw_add_snmp_mgr_from_dict = DeviceType4NwAddSnmpMgr.from_dict(device_type4_nw_add_snmp_mgr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


