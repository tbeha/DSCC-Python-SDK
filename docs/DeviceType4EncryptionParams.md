# DeviceType4EncryptionParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_ekm** | **bool** | Attribute to enable EKM encryption. Make sure to set the EKM server details using the endpoint /api/v1/storage-systems/device-type4/{systemId}/encryption/setekm before setting this attribute to true. | [optional] 
**enable_lkm** | **bool** | This attribute specifies that the desired Key Manager is the Local Key Manager(LKM) for the encryption. If neither the enableEkm or enableLkm attribute is specified on initial encryption enablement, LKM is assumed. This is supported from OS version 10.4.0 or above. | [optional] 
**password** | **str** | Password for the encryption operation. | [optional] 

## Example

```python
from dscc.models.device_type4_encryption_params import DeviceType4EncryptionParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4EncryptionParams from a JSON string
device_type4_encryption_params_instance = DeviceType4EncryptionParams.from_json(json)
# print the JSON string representation of the object
print(DeviceType4EncryptionParams.to_json())

# convert the object into a dict
device_type4_encryption_params_dict = device_type4_encryption_params_instance.to_dict()
# create an instance of DeviceType4EncryptionParams from a dict
device_type4_encryption_params_from_dict = DeviceType4EncryptionParams.from_dict(device_type4_encryption_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


