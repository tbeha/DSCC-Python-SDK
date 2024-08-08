# RemoveReplicationPartners

Request body for deleting replication partner pairs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partners** | [**List[ReplicationPartnerPairAction]**](ReplicationPartnerPairAction.md) | List of replication partner pairs to be deleted | 

## Example

```python
from dscc.models.remove_replication_partners import RemoveReplicationPartners

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveReplicationPartners from a JSON string
remove_replication_partners_instance = RemoveReplicationPartners.from_json(json)
# print the JSON string representation of the object
print(RemoveReplicationPartners.to_json())

# convert the object into a dict
remove_replication_partners_dict = remove_replication_partners_instance.to_dict()
# create an instance of RemoveReplicationPartners from a dict
remove_replication_partners_from_dict = RemoveReplicationPartners.from_dict(remove_replication_partners_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


