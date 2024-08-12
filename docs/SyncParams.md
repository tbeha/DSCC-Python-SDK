# SyncParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_full_sync** | **bool** | Forces full synchronization, even if volumes are already synchronized. This option is only applicable for volume sets with synchronous replication. For SLD, 3DC PP and 3DC APP configurations full synchronization will happen on sync target. | [optional] 
**not_save_resync_snap** | **bool** | Do not save resynchronization snapshot. This option is only applicable for volume sets with asynchronous replication. | [optional] 
**target_name** | **str** | Replication partner name (target name) on which the sync action to be performed. | [optional] 

## Example

```python
from dscc.models.sync_params import SyncParams

# TODO update the JSON string below
json = "{}"
# create an instance of SyncParams from a JSON string
sync_params_instance = SyncParams.from_json(json)
# print the JSON string representation of the object
print(SyncParams.to_json())

# convert the object into a dict
sync_params_dict = sync_params_instance.to_dict()
# create an instance of SyncParams from a dict
sync_params_from_dict = SyncParams.from_dict(sync_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


