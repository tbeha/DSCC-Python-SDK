# ImportCertificateInput

Import Certificate input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authority_chain** | **str** | The authority chain for the new certificate. | 
**certificate** | **str** | The certificate that results from the Certificate Signing Request (CSR). | 

## Example

```python
from dscc.models.import_certificate_input import ImportCertificateInput

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCertificateInput from a JSON string
import_certificate_input_instance = ImportCertificateInput.from_json(json)
# print the JSON string representation of the object
print(ImportCertificateInput.to_json())

# convert the object into a dict
import_certificate_input_dict = import_certificate_input_instance.to_dict()
# create an instance of ImportCertificateInput from a dict
import_certificate_input_from_dict = ImportCertificateInput.from_dict(import_certificate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


