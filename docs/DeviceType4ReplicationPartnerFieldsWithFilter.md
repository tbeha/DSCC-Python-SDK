# DeviceType4ReplicationPartnerFieldsWithFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the replication partner. &#x60;Filter&#x60; | [optional] 
**name** | **str** | Name of the replication partner. &#x60;Filter, Sort&#x60; | [optional] 
**replication_partner_type** | **str** | Link protocol type. &#x60;Filter, Sort&#x60; | [optional] 
**status** | **str** | Status of the partner. Possible values - New, Ready, Unsupported, Failing, Failed or Disabled. &#x60;Filter, Sort&#x60; | [optional] 

## Example

```python
from dscc.models.device_type4_replication_partner_fields_with_filter import DeviceType4ReplicationPartnerFieldsWithFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ReplicationPartnerFieldsWithFilter from a JSON string
device_type4_replication_partner_fields_with_filter_instance = DeviceType4ReplicationPartnerFieldsWithFilter.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ReplicationPartnerFieldsWithFilter.to_json())

# convert the object into a dict
device_type4_replication_partner_fields_with_filter_dict = device_type4_replication_partner_fields_with_filter_instance.to_dict()
# create an instance of DeviceType4ReplicationPartnerFieldsWithFilter from a dict
device_type4_replication_partner_fields_with_filter_from_dict = DeviceType4ReplicationPartnerFieldsWithFilter.from_dict(device_type4_replication_partner_fields_with_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


