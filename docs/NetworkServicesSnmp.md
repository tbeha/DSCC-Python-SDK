# NetworkServicesSnmp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**SnmpMgrDetails**](SnmpMgrDetails.md) |  | [optional] 
**request_uri** | **str** | requestUri for detailed storage object               | [optional] 

## Example

```python
from dscc.models.network_services_snmp import NetworkServicesSnmp

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkServicesSnmp from a JSON string
network_services_snmp_instance = NetworkServicesSnmp.from_json(json)
# print the JSON string representation of the object
print(NetworkServicesSnmp.to_json())

# convert the object into a dict
network_services_snmp_dict = network_services_snmp_instance.to_dict()
# create an instance of NetworkServicesSnmp from a dict
network_services_snmp_from_dict = NetworkServicesSnmp.from_dict(network_services_snmp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


