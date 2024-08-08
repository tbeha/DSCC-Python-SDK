# DeviceType4SupportedProtectionTypes

Response body for supported protection types on an application set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**async_partners** | [**List[DeviceType4ReplicationPartner]**](DeviceType4ReplicationPartner.md) | List of potential replication partners that can be part of asynchronous protection policy | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**is_sld_supported** | **bool** | Shows if SLD is supported or not | [optional] 
**protection_types** | **List[str]** | List of protection policies types that can be configured on the application set Possible values: schedule, async, sync | [optional] 
**request_uri** | **str** | requestUri for supported protection types | [optional] 
**sync_partners** | [**List[DeviceType4ReplicationPartner]**](DeviceType4ReplicationPartner.md) | List of potential replication partners that can be part of synchronous protection policy | [optional] 

## Example

```python
from dscc.models.device_type4_supported_protection_types import DeviceType4SupportedProtectionTypes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SupportedProtectionTypes from a JSON string
device_type4_supported_protection_types_instance = DeviceType4SupportedProtectionTypes.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SupportedProtectionTypes.to_json())

# convert the object into a dict
device_type4_supported_protection_types_dict = device_type4_supported_protection_types_instance.to_dict()
# create an instance of DeviceType4SupportedProtectionTypes from a dict
device_type4_supported_protection_types_from_dict = DeviceType4SupportedProtectionTypes.from_dict(device_type4_supported_protection_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


