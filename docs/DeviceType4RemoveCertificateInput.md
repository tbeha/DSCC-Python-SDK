# DeviceType4RemoveCertificateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | ID of certificate to be deleted | 

## Example

```python
from dscc.models.device_type4_remove_certificate_input import DeviceType4RemoveCertificateInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RemoveCertificateInput from a JSON string
device_type4_remove_certificate_input_instance = DeviceType4RemoveCertificateInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RemoveCertificateInput.to_json())

# convert the object into a dict
device_type4_remove_certificate_input_dict = device_type4_remove_certificate_input_instance.to_dict()
# create an instance of DeviceType4RemoveCertificateInput from a dict
device_type4_remove_certificate_input_from_dict = DeviceType4RemoveCertificateInput.from_dict(device_type4_remove_certificate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


