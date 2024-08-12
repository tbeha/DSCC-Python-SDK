# FriendlyCertificate

Friendly info of the SMTP/mail server certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_from** | [**DeviceType4friendlyCertificateValidFrom**](DeviceType4friendlyCertificateValidFrom.md) |  | [optional] 
**valid_until** | [**DeviceType4friendlyCertificateValidUntil**](DeviceType4friendlyCertificateValidUntil.md) |  | [optional] 
**issued_to** | **str** | Certificate issued to | [optional] 
**issuer** | **str** | Certificate issuer | [optional] 

## Example

```python
from dscc.models.friendly_certificate import FriendlyCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of FriendlyCertificate from a JSON string
friendly_certificate_instance = FriendlyCertificate.from_json(json)
# print the JSON string representation of the object
print(FriendlyCertificate.to_json())

# convert the object into a dict
friendly_certificate_dict = friendly_certificate_instance.to_dict()
# create an instance of FriendlyCertificate from a dict
friendly_certificate_from_dict = FriendlyCertificate.from_dict(friendly_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


