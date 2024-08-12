# DeviceType4RemoveCertificatesInput

Request body for deleting the certificates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | [**List[DeviceType4RemoveCertificateInput]**](DeviceType4RemoveCertificateInput.md) | List of certificate IDs to be deleted | 

## Example

```python
from dscc.models.device_type4_remove_certificates_input import DeviceType4RemoveCertificatesInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4RemoveCertificatesInput from a JSON string
device_type4_remove_certificates_input_instance = DeviceType4RemoveCertificatesInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4RemoveCertificatesInput.to_json())

# convert the object into a dict
device_type4_remove_certificates_input_dict = device_type4_remove_certificates_input_instance.to_dict()
# create an instance of DeviceType4RemoveCertificatesInput from a dict
device_type4_remove_certificates_input_from_dict = DeviceType4RemoveCertificatesInput.from_dict(device_type4_remove_certificates_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


