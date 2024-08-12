# DeviceType4AlertContacts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**List[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**items** | [**List[DeviceType4AlertContactsDetails]**](DeviceType4AlertContactsDetails.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for alert contact details | [optional] 
**system_id** | **str** | SystemId of the storage system | [optional] 
**total** | **int** | Number of contacts | [optional] 

## Example

```python
from dscc.models.device_type4_alert_contacts import DeviceType4AlertContacts

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4AlertContacts from a JSON string
device_type4_alert_contacts_instance = DeviceType4AlertContacts.from_json(json)
# print the JSON string representation of the object
print(DeviceType4AlertContacts.to_json())

# convert the object into a dict
device_type4_alert_contacts_dict = device_type4_alert_contacts_instance.to_dict()
# create an instance of DeviceType4AlertContacts from a dict
device_type4_alert_contacts_from_dict = DeviceType4AlertContacts.from_dict(device_type4_alert_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


