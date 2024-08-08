# AlertContactsDetailsList

Contacts details set to receive alerts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_resource_attributes** | [**PrimeraCommonResourceAttributes**](PrimeraCommonResourceAttributes.md) |  | [optional] 
**company** | **str** | Company | [optional] 
**company_code** | **str** | Company code | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**country** | **str** | Country | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**fax** | **str** | Fax number | [optional] 
**first_name** | **str** | First name | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.  | [optional] 
**id** | **str** | Unique Identifier of the contact | [optional] 
**include_svc_alerts** | **bool** | Email sent to contact shall include service alert | [optional] 
**last_name** | **str** | Last name | [optional] 
**notification_severities** | **List[int]** | Severities of notifications the contact will be notificated. An array of number: 0 - Fatal, 1 - Critical, 2 - Major, 3 - Minor, 4 - Degraded, 5 - Info, 6 - Debug | [optional] 
**preferred_language** | **str** | Preferred language when being contacted or emailed | [optional] 
**primary_email** | **str** | Primary email address | [optional] 
**primary_phone** | **str** | Primary phone | [optional] 
**receive_email** | **bool** | Contact will receive email notifications. This is a deprecated field and will always pass true to be inline with UI. | [optional] 
**receive_grouped** | **bool** | Contact will receive grouped low urgency email notifications | [optional] 
**request_uri** | **str** | requestUri for alert contact details | [optional] 
**secondary_email** | **str** | Secondary email address | [optional] 
**secondary_phone** | **str** | Secondary phone | [optional] 
**system_id** | **str** | SystemId/serialNumber of the array. | [optional] 
**system_support_contact** | **bool** | Contact will be called for any system issues | [optional] 
**type** | **str** | The type of resource | [optional] 

## Example

```python
from dscc.models.alert_contacts_details_list import AlertContactsDetailsList

# TODO update the JSON string below
json = "{}"
# create an instance of AlertContactsDetailsList from a JSON string
alert_contacts_details_list_instance = AlertContactsDetailsList.from_json(json)
# print the JSON string representation of the object
print(AlertContactsDetailsList.to_json())

# convert the object into a dict
alert_contacts_details_list_dict = alert_contacts_details_list_instance.to_dict()
# create an instance of AlertContactsDetailsList from a dict
alert_contacts_details_list_from_dict = AlertContactsDetailsList.from_dict(alert_contacts_details_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


