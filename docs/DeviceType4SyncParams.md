# DeviceType4SyncParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_full_sync** | **bool** | Forces full synchronization, even if volumes are already synchronized. This option is only applicable for volume sets with synchronous replication. | [optional] 

## Example

```python
from dscc.models.device_type4_sync_params import DeviceType4SyncParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceType4SyncParams from a JSON string
device_type4_sync_params_instance = DeviceType4SyncParams.from_json(json)
# print the JSON string representation of the object
print(DeviceType4SyncParams.to_json())

# convert the object into a dict
device_type4_sync_params_dict = device_type4_sync_params_instance.to_dict()
# create an instance of DeviceType4SyncParams from a dict
device_type4_sync_params_from_dict = DeviceType4SyncParams.from_dict(device_type4_sync_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


