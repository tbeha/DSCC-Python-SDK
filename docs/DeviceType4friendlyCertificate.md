# DeviceType4friendlyCertificate

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
from dscc.models.device_type4friendly_certificate import DeviceType4friendlyCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4friendlyCertificate from a JSON string
device_type4friendly_certificate_instance = DeviceType4friendlyCertificate.from_json(json)
# print the JSON string representation of the object
print(DeviceType4friendlyCertificate.to_json())

# convert the object into a dict
device_type4friendly_certificate_dict = device_type4friendly_certificate_instance.to_dict()
# create an instance of DeviceType4friendlyCertificate from a dict
device_type4friendly_certificate_from_dict = DeviceType4friendlyCertificate.from_dict(device_type4friendly_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


