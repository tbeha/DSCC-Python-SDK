# EditIsnsSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isns_enabled** | **bool** | Enable or disable iSNS. | [optional] 
**isns_port** | **int** | Port number for iSNS Server. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**isns_server** | **str** | Hostname or IP Address of iSNS Server. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. | [optional] 

## Example

```python
from dscc.models.edit_isns_settings import EditIsnsSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EditIsnsSettings from a JSON string
edit_isns_settings_instance = EditIsnsSettings.from_json(json)
# print the JSON string representation of the object
print(EditIsnsSettings.to_json())

# convert the object into a dict
edit_isns_settings_dict = edit_isns_settings_instance.to_dict()
# create an instance of EditIsnsSettings from a dict
edit_isns_settings_from_dict = EditIsnsSettings.from_dict(edit_isns_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


