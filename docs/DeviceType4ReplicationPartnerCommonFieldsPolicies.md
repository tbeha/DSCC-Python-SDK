# DeviceType4ReplicationPartnerCommonFieldsPolicies

Any policies that are set for the partner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mirror_config** | **bool** | Duplication of all configurations involving the specified partner. | [optional] 

## Example

```python
from dscc.models.device_type4_replication_partner_common_fields_policies import DeviceType4ReplicationPartnerCommonFieldsPolicies

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4ReplicationPartnerCommonFieldsPolicies from a JSON string
device_type4_replication_partner_common_fields_policies_instance = DeviceType4ReplicationPartnerCommonFieldsPolicies.from_json(json)
# print the JSON string representation of the object
print(DeviceType4ReplicationPartnerCommonFieldsPolicies.to_json())

# convert the object into a dict
device_type4_replication_partner_common_fields_policies_dict = device_type4_replication_partner_common_fields_policies_instance.to_dict()
# create an instance of DeviceType4ReplicationPartnerCommonFieldsPolicies from a dict
device_type4_replication_partner_common_fields_policies_from_dict = DeviceType4ReplicationPartnerCommonFieldsPolicies.from_dict(device_type4_replication_partner_common_fields_policies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


