# DeviceType4snmpMgrDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**snmp** | [**DeviceType4snmpDetails**](DeviceType4snmpDetails.md) |  | [optional] 
**system_id** | **str** | SystemId of the storage system | [optional] 

## Example

```python
from dscc.models.device_type4snmp_mgr_details import DeviceType4snmpMgrDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4snmpMgrDetails from a JSON string
device_type4snmp_mgr_details_instance = DeviceType4snmpMgrDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4snmpMgrDetails.to_json())

# convert the object into a dict
device_type4snmp_mgr_details_dict = device_type4snmp_mgr_details_instance.to_dict()
# create an instance of DeviceType4snmpMgrDetails from a dict
device_type4snmp_mgr_details_from_dict = DeviceType4snmpMgrDetails.from_dict(device_type4snmp_mgr_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


