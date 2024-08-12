# CertificateDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**cert_type** | **str** | Type of array certificate | [optional] 
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**commonname** | **str** | Commonname of the resource | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object  | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**displayname** | **str** | Displayname of the resource | [optional] 
**domain** | **str** | Domain of the resource | [optional] 
**enddate** | [**DeviceType4CertificateDetailsEnddate**](DeviceType4CertificateDetailsEnddate.md) |  | [optional] 
**fingerprint** | **str** | Fingerprint of the resource | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**id** | **str** | Unique Identifier of the resource | [optional] 
**issuer** | **str** | Issuer of the resource | [optional] 
**pem** | **str** | array certificate pem | [optional] 
**request_uri** | **str** | requestUri for detailed certificate object | [optional] 
**serial** | **str** | Serial of the resource | [optional] 
**service** | **str** | Service name of the resource | [optional] 
**signaturetype** | **str** | Signature type of the resource | [optional] 
**startdate** | [**DeviceType4CertificateDetailsStartdate**](DeviceType4CertificateDetailsStartdate.md) |  | [optional] 
**subject** | **str** | Subject of the resource | [optional] 
**subjectaltname** | **str** | Subjectaltname of the resource | [optional] 
**system_id** | **str** | SystemID of the array | [optional] 
**text** | **str** | array certificate text | [optional] 
**type** | **str** | The type of resource. | [optional] 
**uri** | **str** | URI of the resource | [optional] 

## Example

```python
from dscc.models.certificate_details import CertificateDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateDetails from a JSON string
certificate_details_instance = CertificateDetails.from_json(json)
# print the JSON string representation of the object
print(CertificateDetails.to_json())

# convert the object into a dict
certificate_details_dict = certificate_details_instance.to_dict()
# create an instance of CertificateDetails from a dict
certificate_details_from_dict = CertificateDetails.from_dict(certificate_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


