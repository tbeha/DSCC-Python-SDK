# EditSupportSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_analytics_gui** | **bool** | Enable or disable Analytics in Nimble GUI. The data gathered is used to evaluate and improve the product. | [optional] 
**allow_support_tunnel** | **bool** | Enable or disable support tunnel. | [optional] 
**autosupport_enabled** | **bool** | Enable or disable autosupport. | [optional] 

## Example

```python
from dscc.models.edit_support_settings import EditSupportSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EditSupportSettings from a JSON string
edit_support_settings_instance = EditSupportSettings.from_json(json)
# print the JSON string representation of the object
print(EditSupportSettings.to_json())

# convert the object into a dict
edit_support_settings_dict = edit_support_settings_instance.to_dict()
# create an instance of EditSupportSettings from a dict
edit_support_settings_from_dict = EditSupportSettings.from_dict(edit_support_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


