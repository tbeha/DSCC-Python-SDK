# DeviceType4Vasa

Vasa service details for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_details** | [**List[DeviceType4CertDetailsInner]**](DeviceType4CertDetailsInner.md) | A list of certificates associated with the VASA service | [optional] 
**cert_mgmt** | [**DeviceType4CertMgmt**](DeviceType4CertMgmt.md) |  | [optional] 
**cert_subject** | **str** | Certificate subject of the VASA Provider | [optional] 
**cert_thumbprint** | **str** | Certificate thumbprint of the VASA Provider | [optional] 
**cfg_list** | [**List[DeviceType4CfgListInner]**](DeviceType4CfgListInner.md) | A list of key/value pairs describing the configuration of the VASA service | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**enabled** | **bool** | Indicates if the service status is enabled or not | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**https_enabled** | **bool** | Indicates if the vasa https state is enabled or not | [optional] 
**https_port** | **int** | Vasa https port number | [optional] 
**id** | **str** | Unique Identifier of the resource | [optional] 
**mem_usage_mi_b** | **int** | Memory usage of the VASA provider | [optional] 
**more_uris** | [**List[DeviceType4VasaUriInfo]**](DeviceType4VasaUriInfo.md) | List of VASA Service URLs | [optional] 
**server_name** | **str** | Name of the vasa server | [optional] 
**service_status** | **str** | The status of VASA service. | [optional] 
**system_id** | **str** | SystemId of the storage system | [optional] 
**system_wwn** | **str** | WWN of the array | [optional] 
**type** | **str** | The type of resource. | [optional] 
**version** | **str** | Version of the VASA provider | [optional] 

## Example

```python
from dscc.models.device_type4_vasa import DeviceType4Vasa

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4Vasa from a JSON string
device_type4_vasa_instance = DeviceType4Vasa.from_json(json)
# print the JSON string representation of the object
print(DeviceType4Vasa.to_json())

# convert the object into a dict
device_type4_vasa_dict = device_type4_vasa_instance.to_dict()
# create an instance of DeviceType4Vasa from a dict
device_type4_vasa_from_dict = DeviceType4Vasa.from_dict(device_type4_vasa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


