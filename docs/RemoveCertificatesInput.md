# RemoveCertificatesInput

Request body for deleting the certificates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | [**List[RemoveCertificateInput]**](RemoveCertificateInput.md) | List of certificate IDs to be deleted | 

## Example

```python
from dscc.models.remove_certificates_input import RemoveCertificatesInput

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveCertificatesInput from a JSON string
remove_certificates_input_instance = RemoveCertificatesInput.from_json(json)
# print the JSON string representation of the object
print(RemoveCertificatesInput.to_json())

# convert the object into a dict
remove_certificates_input_dict = remove_certificates_input_instance.to_dict()
# create an instance of RemoveCertificatesInput from a dict
remove_certificates_input_from_dict = RemoveCertificatesInput.from_dict(remove_certificates_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


