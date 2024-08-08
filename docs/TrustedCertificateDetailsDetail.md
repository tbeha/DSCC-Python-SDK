# TrustedCertificateDetailsDetail

Detail of the trusted certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | default value of trusted certificate | [optional] 
**key** | **str** | detail key of trusted certificate | [optional] 

## Example

```python
from dscc.models.trusted_certificate_details_detail import TrustedCertificateDetailsDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedCertificateDetailsDetail from a JSON string
trusted_certificate_details_detail_instance = TrustedCertificateDetailsDetail.from_json(json)
# print the JSON string representation of the object
print(TrustedCertificateDetailsDetail.to_json())

# convert the object into a dict
trusted_certificate_details_detail_dict = trusted_certificate_details_detail_instance.to_dict()
# create an instance of TrustedCertificateDetailsDetail from a dict
trusted_certificate_details_detail_from_dict = TrustedCertificateDetailsDetail.from_dict(trusted_certificate_details_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


