# DeviceType4MailsettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mail_host_domain** | **str** | SMTP server&#39;s Host Domain | [optional] 
**mail_host_server** | **str** | SMTP server address/IP | [optional] 
**port** | **int** | SMTP server&#39;s port number | [optional] 
**sender_email_id** | **str** | Sender email address | [optional] 

## Example

```python
from dscc.models.device_type4_mailsettings_input import DeviceType4MailsettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4MailsettingsInput from a JSON string
device_type4_mailsettings_input_instance = DeviceType4MailsettingsInput.from_json(json)
# print the JSON string representation of the object
print(DeviceType4MailsettingsInput.to_json())

# convert the object into a dict
device_type4_mailsettings_input_dict = device_type4_mailsettings_input_instance.to_dict()
# create an instance of DeviceType4MailsettingsInput from a dict
device_type4_mailsettings_input_from_dict = DeviceType4MailsettingsInput.from_dict(device_type4_mailsettings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


