# ReplicationPartnerPairAction

Replication Partner pair input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partner_system_id** | **str** | The ID of the system where the remote replication partner is created. A 42 digit hexadecimal number. | [optional] 
**src_replication_id** | **str** | The ID of the replication partner. A 42 digit hexadecimal number. | [optional] 
**target_replication_id** | **str** | The ID of the remote replication partner. A 42 digit hexadecimal number. | [optional] 

## Example

```python
from dscc.models.replication_partner_pair_action import ReplicationPartnerPairAction

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationPartnerPairAction from a JSON string
replication_partner_pair_action_instance = ReplicationPartnerPairAction.from_json(json)
# print the JSON string representation of the object
print(ReplicationPartnerPairAction.to_json())

# convert the object into a dict
replication_partner_pair_action_dict = replication_partner_pair_action_instance.to_dict()
# create an instance of ReplicationPartnerPairAction from a dict
replication_partner_pair_action_from_dict = ReplicationPartnerPairAction.from_dict(replication_partner_pair_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


