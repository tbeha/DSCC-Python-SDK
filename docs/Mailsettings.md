# Mailsettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**authentication_required** | **str** | Authentication needed for SMTP settings,possible options are:enabled or disabled | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**friendly_cert** | [**FriendlyCertificate**](FriendlyCertificate.md) |  | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.  | [optional] 
**mail_host_domain** | **str** | SMTP server&#39;s Host Domain | [optional] 
**mail_host_server** | **str** | SMTP server address/IP | [optional] 
**port** | **int** | SMTP server&#39;s port number | [optional] 
**request_uri** | **str** | requestUri for mail settings    | [optional] 
**sender_email_id** | **str** | Sender email address | [optional] 
**type** | **str** | The type of resource. | [optional] 
**username** | **str** | SMTP server&#39;s username authentication | [optional] 

## Example

```python
from dscc.models.mailsettings import Mailsettings

# TODO update the JSON string below
json = "{}"
# create an instance of Mailsettings from a JSON string
mailsettings_instance = Mailsettings.from_json(json)
# print the JSON string representation of the object
print(Mailsettings.to_json())

# convert the object into a dict
mailsettings_dict = mailsettings_instance.to_dict()
# create an instance of Mailsettings from a dict
mailsettings_from_dict = Mailsettings.from_dict(mailsettings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


