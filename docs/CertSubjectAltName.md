# CertSubjectAltName

Subject Alternative Name for the certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | **str** | DNS for Subject Alternative Name for the certificate | [optional] 
**ip** | **str** | IP Address for Subject Alternative Name for the certificate | [optional] 
**email** | **str** | Email for Subject Alternative Name for the certificate | [optional] 

## Example

```python
from dscc.models.cert_subject_alt_name import CertSubjectAltName

# TODO update the JSON string below
json = "{}"
# create an instance of CertSubjectAltName from a JSON string
cert_subject_alt_name_instance = CertSubjectAltName.from_json(json)
# print the JSON string representation of the object
print(CertSubjectAltName.to_json())

# convert the object into a dict
cert_subject_alt_name_dict = cert_subject_alt_name_instance.to_dict()
# create an instance of CertSubjectAltName from a dict
cert_subject_alt_name_from_dict = CertSubjectAltName.from_dict(cert_subject_alt_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


