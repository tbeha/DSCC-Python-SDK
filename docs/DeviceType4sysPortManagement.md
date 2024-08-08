# DeviceType4sysPortManagement

Port Management details for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**authentication_required** | **str** | Is authentication required. Allowed values are enabled or disabled | [optional] 
**common_resource_attributes** | [**CommonResourceAttributes**](CommonResourceAttributes.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**default_route_ipv4** | **str** | Default IPV4 route address of the network port | [optional] 
**default_route_ipv6** | **str** | Default IPV6 route address of the network port | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**dns_server** | **str** | DNS Server of the network port | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**id** | **str** | Unique Identifier of the resource | [optional] 
**ip_v4_data** | [**DeviceType4Address**](DeviceType4Address.md) |  | [optional] 
**ip_v6_data** | [**DeviceType4Address**](DeviceType4Address.md) |  | [optional] 
**new_default_route_ipv4** | **str** | New default IPV4 route address of the network port | [optional] 
**new_default_route_ipv6** | **str** | New default IPV6 route address of the network port | [optional] 
**new_ip_v4_data** | [**DeviceType4Address**](DeviceType4Address.md) |  | [optional] 
**new_ipv6_data** | [**DeviceType4Address**](DeviceType4Address.md) |  | [optional] 
**ntp_server** | **str** | NTP Server of the network port | [optional] 
**proxy_port** | **int** | Proxy Server Port. Allowed values are 1-65535 | [optional] 
**proxy_protocol** | **str** | Supported proxy protocols are HTTP, SOCKS4 and SOCKS5. | [optional] 
**proxy_server** | **str** | Proxy server IP address | [optional] 
**proxy_user** | **str** | Username for authentication. (Required only if Authentication required is enabled) | [optional] 
**system_id** | **str** | Serial Number of the array | [optional] 
**type** | **str** | The type of resource. | [optional] 

## Example

```python
from dscc.models.device_type4sys_port_management import DeviceType4sysPortManagement

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4sysPortManagement from a JSON string
device_type4sys_port_management_instance = DeviceType4sysPortManagement.from_json(json)
# print the JSON string representation of the object
print(DeviceType4sysPortManagement.to_json())

# convert the object into a dict
device_type4sys_port_management_dict = device_type4sys_port_management_instance.to_dict()
# create an instance of DeviceType4sysPortManagement from a dict
device_type4sys_port_management_from_dict = DeviceType4sysPortManagement.from_dict(device_type4sys_port_management_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


