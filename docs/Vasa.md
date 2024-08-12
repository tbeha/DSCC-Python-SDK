# Vasa

Vasa service details for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_mgmt** | [**CertMgmt**](CertMgmt.md) |  | [optional] 
**cert_subject** | **str** | Certificate subject of the VASA Provider | [optional] 
**cert_thumbprint** | **str** | Certificate thumbprint of the VASA Provider | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**enabled** | **bool** | Indicates if the service status is enabled or not | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**https_enabled** | **bool** | Indicates if the vasa https state is enabled or not | [optional] 
**https_port** | **int** | Vasa https port number | [optional] 
**id** | **str** | Unique Identifier of the resource | [optional] 
**mem_usage_mi_b** | **int** | Memory usage of the VASA provider | [optional] 
**more_uris** | [**List[VasaUriInfo]**](VasaUriInfo.md) | List of VASA Service URLs  | [optional] 
**server_name** | **str** | Name of the vasa server | [optional] 
**system_id** | **str** | SystemId of the storage system | [optional] 
**system_wwn** | **str** | WWN of the array | [optional] 
**type** | **str** | The type of resource. | [optional] 
**version** | **str** | Version of the VASA provider | [optional] 

## Example

```python
from dscc.models.vasa import Vasa

# TODO update the JSON string below
json = "{}"
# create an instance of Vasa from a JSON string
vasa_instance = Vasa.from_json(json)
# print the JSON string representation of the object
print(Vasa.to_json())

# convert the object into a dict
vasa_dict = vasa_instance.to_dict()
# create an instance of Vasa from a dict
vasa_from_dict = Vasa.from_dict(vasa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


