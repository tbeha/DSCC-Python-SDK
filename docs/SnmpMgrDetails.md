# SnmpMgrDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**snmp** | [**SnmpDetails**](SnmpDetails.md) |  | [optional] 
**system_id** | **str** | SystemId of the storage system | [optional] 

## Example

```python
from dscc.models.snmp_mgr_details import SnmpMgrDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpMgrDetails from a JSON string
snmp_mgr_details_instance = SnmpMgrDetails.from_json(json)
# print the JSON string representation of the object
print(SnmpMgrDetails.to_json())

# convert the object into a dict
snmp_mgr_details_dict = snmp_mgr_details_instance.to_dict()
# create an instance of SnmpMgrDetails from a dict
snmp_mgr_details_from_dict = SnmpMgrDetails.from_dict(snmp_mgr_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


