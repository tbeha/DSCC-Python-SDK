# DeviceType4CertificateDetailsEnddate

End date of the array certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | time in millisecond | [optional] 
**tz** | **str** | timezone | [optional] 

## Example

```python
from dscc.models.device_type4_certificate_details_enddate import DeviceType4CertificateDetailsEnddate

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CertificateDetailsEnddate from a JSON string
device_type4_certificate_details_enddate_instance = DeviceType4CertificateDetailsEnddate.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CertificateDetailsEnddate.to_json())

# convert the object into a dict
device_type4_certificate_details_enddate_dict = device_type4_certificate_details_enddate_instance.to_dict()
# create an instance of DeviceType4CertificateDetailsEnddate from a dict
device_type4_certificate_details_enddate_from_dict = DeviceType4CertificateDetailsEnddate.from_dict(device_type4_certificate_details_enddate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


