# NimbleMoveVolumeToAnotherPoolInput

Input to move Nimble volume to another pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_pool_id** | **str** | ID of the destination pool or folder. Specify a pool ID when the volumes should not be in a folder; otherwise, specify a folder ID and the pool will be derived from the folder. A 42 digit hexadecimal number | 

## Example

```python
from dscc.models.nimble_move_volume_to_another_pool_input import NimbleMoveVolumeToAnotherPoolInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleMoveVolumeToAnotherPoolInput from a JSON string
nimble_move_volume_to_another_pool_input_instance = NimbleMoveVolumeToAnotherPoolInput.from_json(json)
# print the JSON string representation of the object
print(NimbleMoveVolumeToAnotherPoolInput.to_json())

# convert the object into a dict
nimble_move_volume_to_another_pool_input_dict = nimble_move_volume_to_another_pool_input_instance.to_dict()
# create an instance of NimbleMoveVolumeToAnotherPoolInput from a dict
nimble_move_volume_to_another_pool_input_from_dict = NimbleMoveVolumeToAnotherPoolInput.from_dict(nimble_move_volume_to_another_pool_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


