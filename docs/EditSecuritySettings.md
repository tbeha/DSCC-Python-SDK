# EditSecuritySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_inactivity_timeout** | **int** | The amount of time in seconds that the user session is inactive before timing out. User inactivity timeout in second, valid range is from 1 to 43200 (720 minutes). | [optional] 

## Example

```python
from dscc.models.edit_security_settings import EditSecuritySettings

# TODO update the JSON string below
json = "{}"
# create an instance of EditSecuritySettings from a JSON string
edit_security_settings_instance = EditSecuritySettings.from_json(json)
# print the JSON string representation of the object
print(EditSecuritySettings.to_json())

# convert the object into a dict
edit_security_settings_dict = edit_security_settings_instance.to_dict()
# create an instance of EditSecuritySettings from a dict
edit_security_settings_from_dict = EditSecuritySettings.from_dict(edit_security_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


