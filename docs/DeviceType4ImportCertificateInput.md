# DeviceType4ImportCertificateInput

Import Certificate input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authority_chain** | **str** | The authority chain for the new certificate. | 
**certificate** | **str** | The certificate that results from the Certificate Signing Request (CSR). | 
**vc_guid** | **str** | vcGuid of the vCenter. It is supported from OS version 10.4.0 and VASA version 5.0.0.0 | [optional] 

## Example

```python
from dscc.models.device_type4_import_certificate_input import DeviceType4ImportCertificateInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ImportCertificateInput from a JSON string
device_type4_import_certificate_input_instance = DeviceType4ImportCertificateInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ImportCertificateInput.to_json())

# convert the object into a dict
device_type4_import_certificate_input_dict = device_type4_import_certificate_input_instance.to_dict()
# create an instance of DeviceType4ImportCertificateInput from a dict
device_type4_import_certificate_input_from_dict = DeviceType4ImportCertificateInput.from_dict(device_type4_import_certificate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


