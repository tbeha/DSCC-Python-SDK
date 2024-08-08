# EncryptionParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_ekm** | **bool** | Flag to enable EKM encryption. | [optional] 
**password** | **str** | Password for the encryption operation. | [optional] 

## Example

```python
from dscc.models.encryption_params import EncryptionParams

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionParams from a JSON string
encryption_params_instance = EncryptionParams.from_json(json)
# print the JSON string representation of the object
print(EncryptionParams.to_json())

# convert the object into a dict
encryption_params_dict = encryption_params_instance.to_dict()
# create an instance of EncryptionParams from a dict
encryption_params_from_dict = EncryptionParams.from_dict(encryption_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


