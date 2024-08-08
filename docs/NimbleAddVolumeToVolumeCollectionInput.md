# NimbleAddVolumeToVolumeCollectionInput

Add volume to volume collection input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_ids** | **List[Optional[str]]** | Volume ids that need to be added to volume collections. | [optional] 

## Example

```python
from dscc.models.nimble_add_volume_to_volume_collection_input import NimbleAddVolumeToVolumeCollectionInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleAddVolumeToVolumeCollectionInput from a JSON string
nimble_add_volume_to_volume_collection_input_instance = NimbleAddVolumeToVolumeCollectionInput.from_json(json)
# print the JSON string representation of the object
print(NimbleAddVolumeToVolumeCollectionInput.to_json())

# convert the object into a dict
nimble_add_volume_to_volume_collection_input_dict = nimble_add_volume_to_volume_collection_input_instance.to_dict()
# create an instance of NimbleAddVolumeToVolumeCollectionInput from a dict
nimble_add_volume_to_volume_collection_input_from_dict = NimbleAddVolumeToVolumeCollectionInput.from_dict(nimble_add_volume_to_volume_collection_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


