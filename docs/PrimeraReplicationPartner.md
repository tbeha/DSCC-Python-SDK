# PrimeraReplicationPartner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**async_partner** | **str** | Shows asynchronous replication partner associated with SLD configuration. This is applicable only if the parent partner is of sync type. | [optional] 
**id** | **str** | Id of replication partner | [optional] 
**is_active_sync_supported** | **bool** | States if Active-Sync is supported or not | [optional] 
**is_peer_persistance_supported** | **bool** | States if Peer Persistance is supported or not | [optional] 
**min_async_rpo** | **int** | Minimum async RPO value in seconds for asynchronous data replication. | [optional] 
**name** | **str** | Name of replication partner | [optional] 
**resource_uri** | **str** | Resource URI for replication partner | [optional] 
**sync_partner** | **str** | Shows synchronous replication partner associated with SLD configuration. This is applicable only if the parent partner is of async type. | [optional] 

## Example

```python
from dscc.models.primera_replication_partner import PrimeraReplicationPartner

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeraReplicationPartner from a JSON string
primera_replication_partner_instance = PrimeraReplicationPartner.from_json(json)
# print the JSON string representation of the object
print(PrimeraReplicationPartner.to_json())

# convert the object into a dict
primera_replication_partner_dict = primera_replication_partner_instance.to_dict()
# create an instance of PrimeraReplicationPartner from a dict
primera_replication_partner_from_dict = PrimeraReplicationPartner.from_dict(primera_replication_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


