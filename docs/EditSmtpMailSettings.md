# EditSmtpMailSettings

Nimble mail-settings input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**smtp_port** | **int** | Port number of SMTP Server. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**smtp_server** | **str** | Hostname or IP Address of SMTP Server. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. | [optional] 

## Example

```python
from dscc.models.edit_smtp_mail_settings import EditSmtpMailSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EditSmtpMailSettings from a JSON string
edit_smtp_mail_settings_instance = EditSmtpMailSettings.from_json(json)
# print the JSON string representation of the object
print(EditSmtpMailSettings.to_json())

# convert the object into a dict
edit_smtp_mail_settings_dict = edit_smtp_mail_settings_instance.to_dict()
# create an instance of EditSmtpMailSettings from a dict
edit_smtp_mail_settings_from_dict = EditSmtpMailSettings.from_dict(edit_smtp_mail_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


