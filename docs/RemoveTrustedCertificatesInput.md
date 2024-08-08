# RemoveTrustedCertificatesInput

Request body for deleting the trusted certificates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trusted_certificates** | [**List[RemoveTrustedCertificateInput]**](RemoveTrustedCertificateInput.md) | List of certificate IDs to be deleted | 

## Example

```python
from dscc.models.remove_trusted_certificates_input import RemoveTrustedCertificatesInput

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveTrustedCertificatesInput from a JSON string
remove_trusted_certificates_input_instance = RemoveTrustedCertificatesInput.from_json(json)
# print the JSON string representation of the object
print(RemoveTrustedCertificatesInput.to_json())

# convert the object into a dict
remove_trusted_certificates_input_dict = remove_trusted_certificates_input_instance.to_dict()
# create an instance of RemoveTrustedCertificatesInput from a dict
remove_trusted_certificates_input_from_dict = RemoveTrustedCertificatesInput.from_dict(remove_trusted_certificates_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


