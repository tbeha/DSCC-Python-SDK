# TrustedCertParams

Parameters for adding a trusted certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | **str** | Trusted certificate text | 
**type** | **str** | Type of the trusted certificate | 

## Example

```python
from dscc.models.trusted_cert_params import TrustedCertParams

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedCertParams from a JSON string
trusted_cert_params_instance = TrustedCertParams.from_json(json)
# print the JSON string representation of the object
print(TrustedCertParams.to_json())

# convert the object into a dict
trusted_cert_params_dict = trusted_cert_params_instance.to_dict()
# create an instance of TrustedCertParams from a dict
trusted_cert_params_from_dict = TrustedCertParams.from_dict(trusted_cert_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


