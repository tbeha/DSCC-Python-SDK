# DeviceType4cim

CIM service details for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cim_policy** | **str** | Specifies the CIM Policy of CIM server | [optional] 
**cim_state** | **str** | Specifies whether CIM state is active or inactive | [optional] 
**cim_version** | **str** | CIM version information | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**http_port** | **int** | HTTP port number | [optional] 
**http_state** | **bool** | Specifies whether HTTPState is enabled or disabled for CIM Server | [optional] 
**https_port** | **int** | Specifies HTTPS port number | [optional] 
**https_state** | **bool** | Specifies whether HTTPS state is enabled or disabled for cim server | [optional] 
**id** | **str** | Unique Identifier of the resource | [optional] 
**pg_version** | **str** | Information about PGVersion of CIM server | [optional] 
**service_state** | **bool** | Specifies whether service state is enabled or disabled | [optional] 
**slp_port** | **int** | SLPport specification | [optional] 
**slp_state** | **bool** | whether slpstate is enabled or disabled | [optional] 
**system_id** | **str** | SystemId of the storage system | [optional] 
**system_wwn** | **str** | WWN of the array | [optional] 
**type** | **str** | The type of resource. | [optional] 

## Example

```python
from dscc.models.device_type4cim import DeviceType4cim

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4cim from a JSON string
device_type4cim_instance = DeviceType4cim.from_json(json)
# print the JSON string representation of the object
print(DeviceType4cim.to_json())

# convert the object into a dict
device_type4cim_dict = device_type4cim_instance.to_dict()
# create an instance of DeviceType4cim from a dict
device_type4cim_from_dict = DeviceType4cim.from_dict(device_type4cim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


