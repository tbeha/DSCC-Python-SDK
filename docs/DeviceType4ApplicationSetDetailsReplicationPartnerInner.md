# DeviceType4ApplicationSetDetailsReplicationPartnerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_system** | **str** | Replication Partner System | [optional] 
**replication_partner** | **str** | Replication Partner | [optional] 

## Example

```python
from dscc.models.device_type4_application_set_details_replication_partner_inner import DeviceType4ApplicationSetDetailsReplicationPartnerInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ApplicationSetDetailsReplicationPartnerInner from a JSON string
device_type4_application_set_details_replication_partner_inner_instance = DeviceType4ApplicationSetDetailsReplicationPartnerInner.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ApplicationSetDetailsReplicationPartnerInner.to_json())

# convert the object into a dict
device_type4_application_set_details_replication_partner_inner_dict = device_type4_application_set_details_replication_partner_inner_instance.to_dict()
# create an instance of DeviceType4ApplicationSetDetailsReplicationPartnerInner from a dict
device_type4_application_set_details_replication_partner_inner_from_dict = DeviceType4ApplicationSetDetailsReplicationPartnerInner.from_dict(device_type4_application_set_details_replication_partner_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


