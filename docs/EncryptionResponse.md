# EncryptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** | Encryption response | 

## Example

```python
from dscc.models.encryption_response import EncryptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionResponse from a JSON string
encryption_response_instance = EncryptionResponse.from_json(json)
# print the JSON string representation of the object
print(EncryptionResponse.to_json())

# convert the object into a dict
encryption_response_dict = encryption_response_instance.to_dict()
# create an instance of EncryptionResponse from a dict
encryption_response_from_dict = EncryptionResponse.from_dict(encryption_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


