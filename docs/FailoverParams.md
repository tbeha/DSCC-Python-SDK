# FailoverParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discard_new_data** | **bool** | If this set to true and there are multiple targets, the system does not check other targets to see where newer data is available to push. | [optional] 
**force_pp_failover** | **bool** | Specifies that the Peer Persistence failover operation is forced overriding data inconsistency warnings. All I/O to the existing primary volumes should be quiesced when using this option. | [optional] 
**no_snapshot** | **bool** | Specifies that snapshots are not taken of application sets that are switched from secondary to primary. Additionally, existing snapshots are deleted if application sets are switched from primary to secondary. The use of this option may result in a full synchronization of the secondary volumes. | [optional] 
**skip_promote** | **bool** | Specifies that the synchronized snapshots of the protected volume set that are switched from primary to secondary should not be promoted to the base volume. The incorrect use of this option can lead to the primary and secondary volumes not being consistent. | [optional] 
**skip_start** | **bool** | Specifies that replication is not started after failover action is completed. | [optional] 
**skip_sync** | **bool** | Specifies that replication is not synced after failover action is completed. | [optional] 
**target_name** | **str** | Replication partner name on which to failover. | [optional] 

## Example

```python
from dscc.models.failover_params import FailoverParams

# TODO update the JSON string below
json = "{}"
# create an instance of FailoverParams from a JSON string
failover_params_instance = FailoverParams.from_json(json)
# print the JSON string representation of the object
print(FailoverParams.to_json())

# convert the object into a dict
failover_params_dict = failover_params_instance.to_dict()
# create an instance of FailoverParams from a dict
failover_params_from_dict = FailoverParams.from_dict(failover_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


