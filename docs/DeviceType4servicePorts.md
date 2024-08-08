# DeviceType4servicePorts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
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
from dscc.models.device_type4service_ports import DeviceType4servicePorts

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4servicePorts from a JSON string
device_type4service_ports_instance = DeviceType4servicePorts.from_json(json)
# print the JSON string representation of the object
print(DeviceType4servicePorts.to_json())

# convert the object into a dict
device_type4service_ports_dict = device_type4service_ports_instance.to_dict()
# create an instance of DeviceType4servicePorts from a dict
device_type4service_ports_from_dict = DeviceType4servicePorts.from_dict(device_type4service_ports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


