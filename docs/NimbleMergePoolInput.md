# NimbleMergePoolInput

Merge the specified pool into the target pool. All volumes on the specified pool are moved to the target pool and the specified pool is then deleted. All the arrays in the pool are assigned to the target pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | Forcibly merge the specified pool into target pool. Defaults to false. | [optional] 
**target_pool_id** | **str** | ID of the target pool. A 42 digit hexadecimal number. | 

## Example

```python
from dscc.models.nimble_merge_pool_input import NimbleMergePoolInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleMergePoolInput from a JSON string
nimble_merge_pool_input_instance = NimbleMergePoolInput.from_json(json)
# print the JSON string representation of the object
print(NimbleMergePoolInput.to_json())

# convert the object into a dict
nimble_merge_pool_input_dict = nimble_merge_pool_input_instance.to_dict()
# create an instance of NimbleMergePoolInput from a dict
nimble_merge_pool_input_from_dict = NimbleMergePoolInput.from_dict(nimble_merge_pool_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


