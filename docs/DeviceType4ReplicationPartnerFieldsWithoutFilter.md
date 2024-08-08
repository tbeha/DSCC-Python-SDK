# DeviceType4ReplicationPartnerFieldsWithoutFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the replication partner. | [optional] 
**name** | **str** | Name of the replication partner. | [optional] 
**replication_partner_type** | **str** | Link protocol type. | [optional] 
**status** | **str** | Status of the partner. Possible values - New, Ready, Unsupported, Failing, Failed or Disabled. | [optional] 

## Example

```python
from dscc.models.device_type4_replication_partner_fields_without_filter import DeviceType4ReplicationPartnerFieldsWithoutFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ReplicationPartnerFieldsWithoutFilter from a JSON string
device_type4_replication_partner_fields_without_filter_instance = DeviceType4ReplicationPartnerFieldsWithoutFilter.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ReplicationPartnerFieldsWithoutFilter.to_json())

# convert the object into a dict
device_type4_replication_partner_fields_without_filter_dict = device_type4_replication_partner_fields_without_filter_instance.to_dict()
# create an instance of DeviceType4ReplicationPartnerFieldsWithoutFilter from a dict
device_type4_replication_partner_fields_without_filter_from_dict = DeviceType4ReplicationPartnerFieldsWithoutFilter.from_dict(device_type4_replication_partner_fields_without_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


