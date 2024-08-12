# EncryptionSettings

How encryption is configured for this group. Group encryption settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cipher** | **str** | Type of encryption cipher used. Possible values: &#39;aes_256_xts&#39;, &#39;none&#39;. | [optional] 
**encryption_active** | **bool** | Is encryption active (output only). | [optional] 
**encryption_key_manager** | **str** | Is the master key on local or external key manager (output only). Possible values: &#39;external&#39;, &#39;local&#39;. | [optional] 
**master_key_set** | **bool** | Is the master key set (output only). | [optional] 
**mode** | **str** | Mode of encryption. Possible values: &#39;available&#39;, &#39;none&#39;, &#39;secure&#39;. | [optional] 
**scope** | **str** | Encryption scope. Possible values: &#39;volume&#39;, &#39;pool&#39;, &#39;none&#39;, &#39;group&#39;. | [optional] 

## Example

```python
from dscc.models.encryption_settings import EncryptionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionSettings from a JSON string
encryption_settings_instance = EncryptionSettings.from_json(json)
# print the JSON string representation of the object
print(EncryptionSettings.to_json())

# convert the object into a dict
encryption_settings_dict = encryption_settings_instance.to_dict()
# create an instance of EncryptionSettings from a dict
encryption_settings_from_dict = EncryptionSettings.from_dict(encryption_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


