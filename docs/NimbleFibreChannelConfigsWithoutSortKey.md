# NimbleFibreChannelConfigsWithoutSortKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_leader_array** | **str** | Name of the group leader array. String of up to 64 alphanumeric characters, - and . and : are allowed after first character | [optional] 
**id** | **str** | Identifier for the array. A 42 digit hexadecimal number. | [optional] 

## Example

```python
from dscc.models.nimble_fibre_channel_configs_without_sort_key import NimbleFibreChannelConfigsWithoutSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleFibreChannelConfigsWithoutSortKey from a JSON string
nimble_fibre_channel_configs_without_sort_key_instance = NimbleFibreChannelConfigsWithoutSortKey.from_json(json)
# print the JSON string representation of the object
print(NimbleFibreChannelConfigsWithoutSortKey.to_json())

# convert the object into a dict
nimble_fibre_channel_configs_without_sort_key_dict = nimble_fibre_channel_configs_without_sort_key_instance.to_dict()
# create an instance of NimbleFibreChannelConfigsWithoutSortKey from a dict
nimble_fibre_channel_configs_without_sort_key_from_dict = NimbleFibreChannelConfigsWithoutSortKey.from_dict(nimble_fibre_channel_configs_without_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


