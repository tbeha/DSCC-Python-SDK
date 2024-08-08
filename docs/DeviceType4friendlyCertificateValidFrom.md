# DeviceType4friendlyCertificateValidFrom

Certificate Validity start time

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds | [optional] 
**tz** | **str** | time zone | [optional] 

## Example

```python
from dscc.models.device_type4friendly_certificate_valid_from import DeviceType4friendlyCertificateValidFrom

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4friendlyCertificateValidFrom from a JSON string
device_type4friendly_certificate_valid_from_instance = DeviceType4friendlyCertificateValidFrom.from_json(json)
# print the JSON string representation of the object
print(DeviceType4friendlyCertificateValidFrom.to_json())

# convert the object into a dict
device_type4friendly_certificate_valid_from_dict = device_type4friendly_certificate_valid_from_instance.to_dict()
# create an instance of DeviceType4friendlyCertificateValidFrom from a dict
device_type4friendly_certificate_valid_from_from_dict = DeviceType4friendlyCertificateValidFrom.from_dict(device_type4friendly_certificate_valid_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


