# EditProxySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proxy_port** | **int** | Proxy Port of HTTP Proxy Server. Integer value between 0-65535 representing TCP/IP port. | [optional] 
**proxy_server** | **str** | Hostname or IP Address of HTTP Proxy Server. Setting this attribute to an empty string will unset all proxy settings. String of alphanumeric characters, can be an empty string, or valid range must be from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. | [optional] 
**proxy_username** | **str** | Username to authenticate with HTTP Proxy Server. HTTP proxy server username, string up to 255 characters, special characters ([, ], &#x60;, ;, ampersand, tab, space, newline) are not allowed. | [optional] 

## Example

```python
from dscc.models.edit_proxy_settings import EditProxySettings

# TODO update the JSON string below
json = "{}"
# create an instance of EditProxySettings from a JSON string
edit_proxy_settings_instance = EditProxySettings.from_json(json)
# print the JSON string representation of the object
print(EditProxySettings.to_json())

# convert the object into a dict
edit_proxy_settings_dict = edit_proxy_settings_instance.to_dict()
# create an instance of EditProxySettings from a dict
edit_proxy_settings_from_dict = EditProxySettings.from_dict(edit_proxy_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


