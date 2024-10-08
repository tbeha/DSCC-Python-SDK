# AlertContactInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **str** | Company | [optional] 
**company_code** | **str** | Company code | [optional] 
**country** | **str** | Country | [optional] 
**fax** | **str** | Fax number | [optional] 
**first_name** | **str** | First name | [optional] 
**include_svc_alerts** | **bool** | Email sent to contact shall include service alert | [optional] 
**last_name** | **str** | Last name | [optional] 
**notification_severities** | **List[int]** | Severities of notifications the contact will be notificated. An array of number: 0 - Fatal, 1 - Critical, 2 - Major, 3 - Minor, 4 - Degraded, 5 - Info, 6 - Debug | [optional] 
**preferred_language** | **str** | Preferred language when being contacted or emailed | [optional] 
**primary_email** | **str** | Primary email address | [optional] 
**primary_phone** | **str** | Primary phone | [optional] 
**receive_email** | **bool** | Contact will receive email notifications. This is a deprecated field and will always pass true to be inline with UI. | [optional] 
**receive_grouped** | **bool** | Contact will receive grouped low urgency email notifications | [optional] 
**secondary_email** | **str** | Secondary email address | [optional] 
**secondary_phone** | **str** | Secondary phone | [optional] 

## Example

```python
from dscc.models.alert_contact_input import AlertContactInput

# TODO update the JSON string below
json = "{}"
# create an instance of AlertContactInput from a JSON string
alert_contact_input_instance = AlertContactInput.from_json(json)
# print the JSON string representation of the object
print(AlertContactInput.to_json())

# convert the object into a dict
alert_contact_input_dict = alert_contact_input_instance.to_dict()
# create an instance of AlertContactInput from a dict
alert_contact_input_from_dict = AlertContactInput.from_dict(alert_contact_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


