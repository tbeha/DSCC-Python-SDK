# MailsettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mail_host_domain** | **str** | SMTP server&#39;s Host Domain | [optional] 
**mail_host_server** | **str** | SMTP server address/IP | [optional] 
**port** | **int** | SMTP server&#39;s port number | [optional] 
**sender_email_id** | **str** | Sender email address | [optional] 

## Example

```python
from dscc.models.mailsettings_input import MailsettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of MailsettingsInput from a JSON string
mailsettings_input_instance = MailsettingsInput.from_json(json)
# print the JSON string representation of the object
print(MailsettingsInput.to_json())

# convert the object into a dict
mailsettings_input_dict = mailsettings_input_instance.to_dict()
# create an instance of MailsettingsInput from a dict
mailsettings_input_from_dict = MailsettingsInput.from_dict(mailsettings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


