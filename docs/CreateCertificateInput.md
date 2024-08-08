# CreateCertificateInput

Create Certificate input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authority_chain** | **str** | The authority chain for Quorum Witness server certificate. | [optional] 
**common_name** | **str** | CommonName for the certificate. | [optional] 
**country** | **str** | Two-letter code for the country where organization is located. | [optional] 
**days** | **int** | Number of days valid for the certificate. | [optional] 
**key_length** | **int** | Key length for the certificate. | [optional] 
**locality** | **str** | Locality where organization is located. | [optional] 
**organization** | **str** | Organization for the certificate | [optional] 
**organization_unit** | **str** | Division of organization handling the certificate. | [optional] 
**province** | **str** | Province where organization is located. | [optional] 
**service** | **str** | Name of service the certificate is for. | 
**subject_alt_name** | [**CertSubjectAltName**](CertSubjectAltName.md) |  | [optional] 
**type** | **str** | Type of certificate to create. | 

## Example

```python
from dscc.models.create_certificate_input import CreateCertificateInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCertificateInput from a JSON string
create_certificate_input_instance = CreateCertificateInput.from_json(json)
# print the JSON string representation of the object
print(CreateCertificateInput.to_json())

# convert the object into a dict
create_certificate_input_dict = create_certificate_input_instance.to_dict()
# create an instance of CreateCertificateInput from a dict
create_certificate_input_from_dict = CreateCertificateInput.from_dict(create_certificate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


