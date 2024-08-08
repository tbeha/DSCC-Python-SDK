# RestoreParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_snapshot** | **bool** | Specifies that snapshots are not taken of application sets that are switched from secondary to primary. Additionally, existing snapshots are deleted if application sets are switched from primary to secondary. The use of this option may result in a full synchronization of the secondary volumes. | [optional] 
**skip_start** | **bool** | Specifies that protection is not started after restore action is completed. | [optional] 
**skip_sync** | **bool** | Specifies that protection is not synced after restore action is completed. | [optional] 
**target_name** | **str** | Replication partner name (target name) on which the restore action to be performed. | [optional] 

## Example

```python
from dscc.models.restore_params import RestoreParams

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreParams from a JSON string
restore_params_instance = RestoreParams.from_json(json)
# print the JSON string representation of the object
print(RestoreParams.to_json())

# convert the object into a dict
restore_params_dict = restore_params_instance.to_dict()
# create an instance of RestoreParams from a dict
restore_params_from_dict = RestoreParams.from_dict(restore_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


