# NimbleRemoveVolumeFromVolumeCollectionInput

Remove volume from volume collection input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_ids** | **List[Optional[str]]** | Volume ids that need to be remove from volume collections. | [optional] 

## Example

```python
from dscc.models.nimble_remove_volume_from_volume_collection_input import NimbleRemoveVolumeFromVolumeCollectionInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleRemoveVolumeFromVolumeCollectionInput from a JSON string
nimble_remove_volume_from_volume_collection_input_instance = NimbleRemoveVolumeFromVolumeCollectionInput.from_json(json)
# print the JSON string representation of the object
print(NimbleRemoveVolumeFromVolumeCollectionInput.to_json())

# convert the object into a dict
nimble_remove_volume_from_volume_collection_input_dict = nimble_remove_volume_from_volume_collection_input_instance.to_dict()
# create an instance of NimbleRemoveVolumeFromVolumeCollectionInput from a dict
nimble_remove_volume_from_volume_collection_input_from_dict = NimbleRemoveVolumeFromVolumeCollectionInput.from_dict(nimble_remove_volume_from_volume_collection_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


