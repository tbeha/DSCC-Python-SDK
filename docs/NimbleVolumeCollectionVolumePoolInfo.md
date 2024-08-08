# NimbleVolumeCollectionVolumePoolInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_id** | **str** | ID of the pool to which the volume belongs to. | [optional] 
**pool_name** | **str** | Name of the pool to which volume belongs to. | [optional] 
**vol_id** | **str** | ID of the volume. | [optional] 
**vol_name** | **str** | Name of the volume. | [optional] 
**volume_creator_id** | **str** | Originator id for the associated volume. | [optional] 
**volume_creator_name** | **str** | Originator name for the associated volume. | [optional] 

## Example

```python
from dscc.models.nimble_volume_collection_volume_pool_info import NimbleVolumeCollectionVolumePoolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleVolumeCollectionVolumePoolInfo from a JSON string
nimble_volume_collection_volume_pool_info_instance = NimbleVolumeCollectionVolumePoolInfo.from_json(json)
# print the JSON string representation of the object
print(NimbleVolumeCollectionVolumePoolInfo.to_json())

# convert the object into a dict
nimble_volume_collection_volume_pool_info_dict = nimble_volume_collection_volume_pool_info_instance.to_dict()
# create an instance of NimbleVolumeCollectionVolumePoolInfo from a dict
nimble_volume_collection_volume_pool_info_from_dict = NimbleVolumeCollectionVolumePoolInfo.from_dict(nimble_volume_collection_volume_pool_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


