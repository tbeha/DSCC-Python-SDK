# SyncTime

Last synchronization time in milliseconds since epoch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** | Epoch time in milliseconds. | [optional] 
**tz** | **str** | Time zone name | [optional] 

## Example

```python
from dscc.models.sync_time import SyncTime

# TODO update the JSON string below
json = "{}"
# create an instance of SyncTime from a JSON string
sync_time_instance = SyncTime.from_json(json)
# print the JSON string representation of the object
print(SyncTime.to_json())

# convert the object into a dict
sync_time_dict = sync_time_instance.to_dict()
# create an instance of SyncTime from a dict
sync_time_from_dict = SyncTime.from_dict(sync_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


