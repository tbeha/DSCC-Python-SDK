# OfflineClone

Offline clone of a volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_volume** | [**CreateVolume**](CreateVolume.md) |  | [optional] 
**enable_resync** | **bool** | Specify to save a snapshot for fast resynchronization. | [optional] 
**use_existing_volume** | **bool** | Specify to use existing volume or create a new volume for clone. | [optional] 

## Example

```python
from dscc.models.offline_clone import OfflineClone

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineClone from a JSON string
offline_clone_instance = OfflineClone.from_json(json)
# print the JSON string representation of the object
print(OfflineClone.to_json())

# convert the object into a dict
offline_clone_dict = offline_clone_instance.to_dict()
# create an instance of OfflineClone from a dict
offline_clone_from_dict = OfflineClone.from_dict(offline_clone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


