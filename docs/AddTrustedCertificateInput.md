# AddTrustedCertificateInput

Request body for adding a trusted certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action to perform with trusted certificate | 
**parameters** | [**TrustedCertParams**](TrustedCertParams.md) |  | 

## Example

```python
from dscc.models.add_trusted_certificate_input import AddTrustedCertificateInput

# TODO update the JSON string below
json = "{}"
# create an instance of AddTrustedCertificateInput from a JSON string
add_trusted_certificate_input_instance = AddTrustedCertificateInput.from_json(json)
# print the JSON string representation of the object
print(AddTrustedCertificateInput.to_json())

# convert the object into a dict
add_trusted_certificate_input_dict = add_trusted_certificate_input_instance.to_dict()
# create an instance of AddTrustedCertificateInput from a dict
add_trusted_certificate_input_from_dict = AddTrustedCertificateInput.from_dict(add_trusted_certificate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


