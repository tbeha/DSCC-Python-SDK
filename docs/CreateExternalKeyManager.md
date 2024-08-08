# CreateExternalKeyManager

Create external key manager input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | String of up to 255 printable ASCII characters. Example: &#39;99.9999% availability&#39;. | [optional] 
**hostname** | **str** | Hostname or IP Address for the External Key Manager. Plain string. | 
**name** | **str** | Name of external key manager. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | 
**password** | **str** | External Key Manager user password. String up to 255 printable characters. String of 8 to 255 printable characters excluding ampersand and ;[] | 
**port** | **int** | Positive integer value up to 65535 representing External key manager port. | 
**protocol** | **str** | Possible values: &#39;KMIP1_0&#39;, &#39;KMIP1_1&#39;, &#39;KMIP1_2&#39;, &#39;KMIP1_3&#39;. | 
**username** | **str** | External key manager username. String of up to 255 printable ASCII characters. | [optional] 

## Example

```python
from dscc.models.create_external_key_manager import CreateExternalKeyManager

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExternalKeyManager from a JSON string
create_external_key_manager_instance = CreateExternalKeyManager.from_json(json)
# print the JSON string representation of the object
print(CreateExternalKeyManager.to_json())

# convert the object into a dict
create_external_key_manager_dict = create_external_key_manager_instance.to_dict()
# create an instance of CreateExternalKeyManager from a dict
create_external_key_manager_from_dict = CreateExternalKeyManager.from_dict(create_external_key_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


