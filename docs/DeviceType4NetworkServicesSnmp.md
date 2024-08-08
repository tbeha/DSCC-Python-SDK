# DeviceType4NetworkServicesSnmp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**DeviceType4snmpMgrDetails**](DeviceType4snmpMgrDetails.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object               | [optional] 

## Example

```python
from dscc.models.device_type4_network_services_snmp import DeviceType4NetworkServicesSnmp

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4NetworkServicesSnmp from a JSON string
device_type4_network_services_snmp_instance = DeviceType4NetworkServicesSnmp.from_json(json)
# print the JSON string representation of the object
print(DeviceType4NetworkServicesSnmp.to_json())

# convert the object into a dict
device_type4_network_services_snmp_dict = device_type4_network_services_snmp_instance.to_dict()
# create an instance of DeviceType4NetworkServicesSnmp from a dict
device_type4_network_services_snmp_from_dict = DeviceType4NetworkServicesSnmp.from_dict(device_type4_network_services_snmp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


