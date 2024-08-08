# TrustedCertificateDetailsEnddate

End date of the trusted certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | time in millisecond | [optional] 
**tz** | **str** | timezone | [optional] 

## Example

```python
from dscc.models.trusted_certificate_details_enddate import TrustedCertificateDetailsEnddate

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedCertificateDetailsEnddate from a JSON string
trusted_certificate_details_enddate_instance = TrustedCertificateDetailsEnddate.from_json(json)
# print the JSON string representation of the object
print(TrustedCertificateDetailsEnddate.to_json())

# convert the object into a dict
trusted_certificate_details_enddate_dict = trusted_certificate_details_enddate_instance.to_dict()
# create an instance of TrustedCertificateDetailsEnddate from a dict
trusted_certificate_details_enddate_from_dict = TrustedCertificateDetailsEnddate.from_dict(trusted_certificate_details_enddate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


