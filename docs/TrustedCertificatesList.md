# TrustedCertificatesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**commonname** | **str** | Displayname of the resource | [optional] 
**detail** | [**TrustedCertificateDetailsDetail**](TrustedCertificateDetailsDetail.md) |  | [optional] 
**domain** | **str** | Domain of the resource | [optional] 
**enddate** | [**TrustedCertificateDetailsEnddate**](TrustedCertificateDetailsEnddate.md) |  | [optional] 
**fingerprint** | **str** | Fingerprint of the resource | [optional] 
**hash** | **str** | Hash of the resource | [optional] 
**id** | **str** | Unique Identifier of the resource | [optional] 
**issuer** | **str** | Issuer of the resource | [optional] 
**isvalid** | **bool** | validity of the resource | [optional] 
**key_usage** | **str** | key usage of the resource | [optional] 
**pem** | **str** | trusted certificate pem | [optional] 
**serial** | **str** | Serial of the resource | [optional] 
**signaturetype** | **str** | Signature type of the resource | [optional] 
**startdate** | [**TrustedCertificateDetailsStartdate**](TrustedCertificateDetailsStartdate.md) |  | [optional] 
**subject** | **str** | Subject of the resource | [optional] 
**system_id** | **str** | SystemID of the array | [optional] 
**type** | **str** | The type of resource. | [optional] 
**uri** | **str** | URI of the resource | [optional] 

## Example

```python
from dscc.models.trusted_certificates_list import TrustedCertificatesList

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedCertificatesList from a JSON string
trusted_certificates_list_instance = TrustedCertificatesList.from_json(json)
# print the JSON string representation of the object
print(TrustedCertificatesList.to_json())

# convert the object into a dict
trusted_certificates_list_dict = trusted_certificates_list_instance.to_dict()
# create an instance of TrustedCertificatesList from a dict
trusted_certificates_list_from_dict = TrustedCertificatesList.from_dict(trusted_certificates_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


