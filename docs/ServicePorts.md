# ServicePorts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**domain** | **str** | domain of the service port object | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | uid (Unique identifier) for the service port object | [optional] 
**ipv4address** | **str** | ipv4address of the service port object &#x60;Filter&#x60; | [optional] 
**ipv4netmask** | **str** | ipv4 net mask of the service port object | [optional] 
**ipv6address** | **str** | ipv6address of the service port object &#x60;Filter&#x60; | [optional] 
**ipv6vnetmask** | **str** | ipv6 net mask for the service port objectt | [optional] 
**mode** | **str** | mode for the service port object | [optional] 
**name** | **str** | display name of the service port object | [optional] 
**node** | **str** | node for the service port object | [optional] 
**resource_uri** | **str** | resourceUri for detailed service ports object | [optional] 
**system_id** | **str** | SystemUid/serialNumber of the array. | [optional] 
**type** | **str** | type | [optional] 

## Example

```python
from dscc.models.service_ports import ServicePorts

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePorts from a JSON string
service_ports_instance = ServicePorts.from_json(json)
# print the JSON string representation of the object
print(ServicePorts.to_json())

# convert the object into a dict
service_ports_dict = service_ports_instance.to_dict()
# create an instance of ServicePorts from a dict
service_ports_from_dict = ServicePorts.from_dict(service_ports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


