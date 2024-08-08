# DeviceType4ContactsDetails

Contacts details set to receive alerts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **str** | Company | [optional] 
**company_code** | **str** | Company code | [optional] 
**country** | **str** | Country | [optional] 
**fax** | **str** | Fax number | [optional] 
**first_name** | **str** | First name | [optional] 
**id** | **str** | Unique Identifier of the contact and this can not be changed | [optional] 
**include_svc_alerts** | **bool** | Email sent to contact shall include service alert | [optional] 
**last_name** | **str** | Last name | [optional] 
**notification_severities** | **List[int]** | Severities of notifications the contact will be notificated. An array of number: 0 - Fatal, 1 - Critical, 2 - Major, 3 - Minor, 4 - Degraded, 5 - Info, 6 - Debug | [optional] 
**preferred_language** | **str** | Preferred language when being contacted or emailed | [optional] 
**primary_email** | **str** | Primary email address | [optional] 
**primary_phone** | **str** | Primary phone | [optional] 
**receive_email** | **bool** | Contact will receive email notifications | [optional] 
**receive_grouped** | **bool** | Contact will receive grouped low urgency email notifications | [optional] 
**secondary_email** | **str** | Secondary email address | [optional] 
**secondary_phone** | **str** | Secondary phone | [optional] 
**system_id** | **str** | SystemId/serialNumber of the array and this can not be changed | [optional] 
**system_support_contact** | **bool** | Contact will be called for any system issues | [optional] 

## Example

```python
from dscc.models.device_type4_contacts_details import DeviceType4ContactsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ContactsDetails from a JSON string
device_type4_contacts_details_instance = DeviceType4ContactsDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ContactsDetails.to_json())

# convert the object into a dict
device_type4_contacts_details_dict = device_type4_contacts_details_instance.to_dict()
# create an instance of DeviceType4ContactsDetails from a dict
device_type4_contacts_details_from_dict = DeviceType4ContactsDetails.from_dict(device_type4_contacts_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


