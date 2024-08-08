# NimblePinnedVolumeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size_pinned_cache_bytes** | **int** | Total pinned cache size of the volume in bytes. | [optional] 
**agent_type** | **str** | Agent type of the volume. Possible values: &#39;none&#39;, &#39;smis&#39;, &#39;vvol&#39;, &#39;openstack&#39;. | [optional] 
**has_locked_snapshots** | **bool** | To verify a volume has an immutable snapshot or not. | [optional] 
**id** | **str** | Identifier of volume. A 42 digit hexadecimal number. | [optional] 
**name** | **str** | Name of volume. | [optional] 
**vol_id** | **str** | Identifier of volume. A 42 digit hexadecimal number. | [optional] 
**vol_name** | **str** | Name of volume. | [optional] 
**volume_creator_id** | **str** | Originator id for the associated volume. | [optional] 
**volume_creator_name** | **str** | Originator name for the associated volume. | [optional] 

## Example

```python
from dscc.models.nimble_pinned_volume_info import NimblePinnedVolumeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NimblePinnedVolumeInfo from a JSON string
nimble_pinned_volume_info_instance = NimblePinnedVolumeInfo.from_json(json)
# print the JSON string representation of the object
print(NimblePinnedVolumeInfo.to_json())

# convert the object into a dict
nimble_pinned_volume_info_dict = nimble_pinned_volume_info_instance.to_dict()
# create an instance of NimblePinnedVolumeInfo from a dict
nimble_pinned_volume_info_from_dict = NimblePinnedVolumeInfo.from_dict(nimble_pinned_volume_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


