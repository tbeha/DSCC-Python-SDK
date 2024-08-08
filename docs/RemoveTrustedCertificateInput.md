# RemoveTrustedCertificateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trusted_certificate** | **str** | ID of certificate to be deleted | 

## Example

```python
from dscc.models.remove_trusted_certificate_input import RemoveTrustedCertificateInput

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveTrustedCertificateInput from a JSON string
remove_trusted_certificate_input_instance = RemoveTrustedCertificateInput.from_json(json)
# print the JSON string representation of the object
print(RemoveTrustedCertificateInput.to_json())

# convert the object into a dict
remove_trusted_certificate_input_dict = remove_trusted_certificate_input_instance.to_dict()
# create an instance of RemoveTrustedCertificateInput from a dict
remove_trusted_certificate_input_from_dict = RemoveTrustedCertificateInput.from_dict(remove_trusted_certificate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


