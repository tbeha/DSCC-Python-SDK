# AlertContacts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**items** | [**List[AlertContactsDetails]**](AlertContactsDetails.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for alert contact details | [optional] 
**system_id** | **str** | SystemId of the storage system | [optional] 
**total** | **int** | Number of contacts | [optional] 

## Example

```python
from dscc.models.alert_contacts import AlertContacts

# TODO update the JSON string below
json = "{}"
# create an instance of AlertContacts from a JSON string
alert_contacts_instance = AlertContacts.from_json(json)
# print the JSON string representation of the object
print(AlertContacts.to_json())

# convert the object into a dict
alert_contacts_dict = alert_contacts_instance.to_dict()
# create an instance of AlertContacts from a dict
alert_contacts_from_dict = AlertContacts.from_dict(alert_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


