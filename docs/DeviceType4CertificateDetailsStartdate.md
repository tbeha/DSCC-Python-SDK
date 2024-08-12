# DeviceType4CertificateDetailsStartdate

Start date of the array certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | time in millisecond | [optional] 
**tz** | **str** | timezone | [optional] 

## Example

```python
from dscc.models.device_type4_certificate_details_startdate import DeviceType4CertificateDetailsStartdate

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4CertificateDetailsStartdate from a JSON string
device_type4_certificate_details_startdate_instance = DeviceType4CertificateDetailsStartdate.from_json(json)
# print the JSON string representation of the object
print(DeviceType4CertificateDetailsStartdate.to_json())

# convert the object into a dict
device_type4_certificate_details_startdate_dict = device_type4_certificate_details_startdate_instance.to_dict()
# create an instance of DeviceType4CertificateDetailsStartdate from a dict
device_type4_certificate_details_startdate_from_dict = DeviceType4CertificateDetailsStartdate.from_dict(device_type4_certificate_details_startdate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


