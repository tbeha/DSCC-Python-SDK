# RemoveCertificateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | ID of certificate to be deleted | 

## Example

```python
from dscc.models.remove_certificate_input import RemoveCertificateInput

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveCertificateInput from a JSON string
remove_certificate_input_instance = RemoveCertificateInput.from_json(json)
# print the JSON string representation of the object
print(RemoveCertificateInput.to_json())

# convert the object into a dict
remove_certificate_input_dict = remove_certificate_input_instance.to_dict()
# create an instance of RemoveCertificateInput from a dict
remove_certificate_input_from_dict = RemoveCertificateInput.from_dict(remove_certificate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


