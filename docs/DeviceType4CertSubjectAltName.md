# DeviceType4CertSubjectAltName

Subject Alternative Name for the certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | **str** | DNS for Subject Alternative Name for the certificate | [optional] 
**ip** | **str** | IP Address for Subject Alternative Name for the certificate | [optional] 
**email** | **str** | Email for Subject Alternative Name for the certificate | [optional] 

## Example

```python
from dscc.models.device_type4_cert_subject_alt_name import DeviceType4CertSubjectAltName

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CertSubjectAltName from a JSON string
device_type4_cert_subject_alt_name_instance = DeviceType4CertSubjectAltName.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CertSubjectAltName.to_json())

# convert the object into a dict
device_type4_cert_subject_alt_name_dict = device_type4_cert_subject_alt_name_instance.to_dict()
# create an instance of DeviceType4CertSubjectAltName from a dict
device_type4_cert_subject_alt_name_from_dict = DeviceType4CertSubjectAltName.from_dict(device_type4_cert_subject_alt_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


