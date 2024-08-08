# NimbleEditPoolInput

Update pool attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_list** | [**List[EditPoolNimbleArrayDetail]**](EditPoolNimbleArrayDetail.md) | List of arrays identified by their IDs, in the pool. | [optional] 
**dedupe_all_volumes** | **bool** | Indicates if dedupe is enabled by default for new volumes on this pool. | [optional] 
**dedupe_capable** | **bool** | Indicates whether the pool is capable of hosting deduped volumes. | [optional] 
**description** | **str** | Text description of pool. String of up to 255 printable ASCII characters. | [optional] 
**force** | **bool** | Forcibly delete the specified pool even if it contains deleted volumes whose space is being reclaimed. Forcibly remove an array from array_list via an update operation even if the array is not reachable. There should no volumes currently in the pool for the forced update operation to succeed. | [optional] 
**is_default** | **bool** | Indicates if this is the default pool. | [optional] 
**name** | **str** | Name of pool. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | 

## Example

```python
from dscc.models.nimble_edit_pool_input import NimbleEditPoolInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleEditPoolInput from a JSON string
nimble_edit_pool_input_instance = NimbleEditPoolInput.from_json(json)
# print the JSON string representation of the object
print(NimbleEditPoolInput.to_json())

# convert the object into a dict
nimble_edit_pool_input_dict = nimble_edit_pool_input_instance.to_dict()
# create an instance of NimbleEditPoolInput from a dict
nimble_edit_pool_input_from_dict = NimbleEditPoolInput.from_dict(nimble_edit_pool_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


