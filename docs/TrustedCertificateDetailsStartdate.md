# TrustedCertificateDetailsStartdate

Start date of the trusted certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | time in millisecond | [optional] 
**tz** | **str** | timezone | [optional] 

## Example

```python
from dscc.models.trusted_certificate_details_startdate import TrustedCertificateDetailsStartdate

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedCertificateDetailsStartdate from a JSON string
trusted_certificate_details_startdate_instance = TrustedCertificateDetailsStartdate.from_json(json)
# print the JSON string representation of the object
print(TrustedCertificateDetailsStartdate.to_json())

# convert the object into a dict
trusted_certificate_details_startdate_dict = trusted_certificate_details_startdate_instance.to_dict()
# create an instance of TrustedCertificateDetailsStartdate from a dict
trusted_certificate_details_startdate_from_dict = TrustedCertificateDetailsStartdate.from_dict(trusted_certificate_details_startdate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


