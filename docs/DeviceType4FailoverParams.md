# DeviceType4FailoverParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_pp_failover** | **bool** | Specifies that the Peer Persistence failover operation is forced overriding data inconsistency warnings. All I/O to the existing primary volumes should be quiesced when using this option. | [optional] 
**no_snapshot** | **bool** | Specifies that snapshots are not taken of application sets that are switched from secondary to primary. Additionally, existing snapshots are deleted if application sets are switched from primary to secondary. The use of this option may result in a full synchronization of the secondary volumes. | [optional] 
**skip_promote** | **bool** | Specifies that the synchronized snapshots of the protected volume set that are switched from primary to secondary should not be promoted to the base volume. The incorrect use of this option can lead to the primary and secondary volumes not being consistent. | [optional] 
**target_name** | **str** | Replication partner name on which to failover. | [optional] 

## Example

```python
from dscc.models.device_type4_failover_params import DeviceType4FailoverParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4FailoverParams from a JSON string
device_type4_failover_params_instance = DeviceType4FailoverParams.from_json(json)
# print the JSON string representation of the object
print(DeviceType4FailoverParams.to_json())

# convert the object into a dict
device_type4_failover_params_dict = device_type4_failover_params_instance.to_dict()
# create an instance of DeviceType4FailoverParams from a dict
device_type4_failover_params_from_dict = DeviceType4FailoverParams.from_dict(device_type4_failover_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


