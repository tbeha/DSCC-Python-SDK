# NwAddSnmpMgr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snmp_config** | [**List[SnmpConfigParams]**](SnmpConfigParams.md) | Specify the SNMP params | [optional] 

## Example

```python
from dscc.models.nw_add_snmp_mgr import NwAddSnmpMgr

# TODO update the JSON string below
json = "{}"
# create an instance of NwAddSnmpMgr from a JSON string
nw_add_snmp_mgr_instance = NwAddSnmpMgr.from_json(json)
# print the JSON string representation of the object
print(NwAddSnmpMgr.to_json())

# convert the object into a dict
nw_add_snmp_mgr_dict = nw_add_snmp_mgr_instance.to_dict()
# create an instance of NwAddSnmpMgr from a dict
nw_add_snmp_mgr_from_dict = NwAddSnmpMgr.from_dict(nw_add_snmp_mgr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


