# EditAlertSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_from_email_addr** | **str** | From email address to use while sending emails. Case insensitive email address. | [optional] 
**alert_min_level** | **str** | Minimum level of alert to be notified. Possible values: &#39;info&#39;, &#39;notice&#39;, &#39;warning&#39;, &#39;critical&#39;. | [optional] 
**alert_to_email_addrs** | **str** | Comma-separated list of email addresss to receive emails. | [optional] 
**send_alert_to_support** | **bool** | Enable or disable alert to support | [optional] 

## Example

```python
from dscc.models.edit_alert_settings import EditAlertSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EditAlertSettings from a JSON string
edit_alert_settings_instance = EditAlertSettings.from_json(json)
# print the JSON string representation of the object
print(EditAlertSettings.to_json())

# convert the object into a dict
edit_alert_settings_dict = edit_alert_settings_instance.to_dict()
# create an instance of EditAlertSettings from a dict
edit_alert_settings_from_dict = EditAlertSettings.from_dict(edit_alert_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


