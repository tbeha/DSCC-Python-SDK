# EditExternalKeyManager

Edit Nimble external key manager input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | String of up to 255 printable ASCII characters. Example: &#39;99.9999% availability&#39;. | [optional] 
**hostname** | **str** | Hostname or IP Address for the External Key Manager. Plain string. | [optional] 
**id** | **str** | Identifier for the External key manager. A 42 digit hexadecimal number. | [optional] 
**name** | **str** | Name of external key manager. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**password** | **str** | \&quot;External Key Manager user password. String up to 255 printable characters. String of 8 to 255 printable characters excluding ampersand and ;[]\&quot; | [optional] 
**port** | **int** | Positive integer value up to 65535 representing External key manager port. | [optional] 
**protocol** | **str** | Possible values: &#39;KMIP1_0&#39;, &#39;KMIP1_1&#39;, &#39;KMIP1_2&#39;, &#39;KMIP1_3&#39;. | [optional] 
**username** | **str** | External key manager username. String of up to 255 printable ASCII characters. | [optional] 

## Example

```python
from dscc.models.edit_external_key_manager import EditExternalKeyManager

# TODO update the JSON string below
json = "{}"
# create an instance of EditExternalKeyManager from a JSON string
edit_external_key_manager_instance = EditExternalKeyManager.from_json(json)
# print the JSON string representation of the object
print(EditExternalKeyManager.to_json())

# convert the object into a dict
edit_external_key_manager_dict = edit_external_key_manager_instance.to_dict()
# create an instance of EditExternalKeyManager from a dict
edit_external_key_manager_from_dict = EditExternalKeyManager.from_dict(edit_external_key_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


