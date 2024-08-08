# NimbleCreatePoolInput

Create a pool with given input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_list** | [**List[CreatePoolNimbleArrayDetail]**](CreatePoolNimbleArrayDetail.md) | List of arrays identified by their IDs, in the pool. | 
**dedupe_all_volumes** | **bool** | Indicates if dedupe is enabled by default for new volumes on this pool. Defaults to false. | [optional] 
**description** | **str** | Text description of pool. String of up to 255 printable ASCII characters. Defaults to empty string. | [optional] 
**name** | **str** | Name of pool. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | 

## Example

```python
from dscc.models.nimble_create_pool_input import NimbleCreatePoolInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleCreatePoolInput from a JSON string
nimble_create_pool_input_instance = NimbleCreatePoolInput.from_json(json)
# print the JSON string representation of the object
print(NimbleCreatePoolInput.to_json())

# convert the object into a dict
nimble_create_pool_input_dict = nimble_create_pool_input_instance.to_dict()
# create an instance of NimbleCreatePoolInput from a dict
nimble_create_pool_input_from_dict = NimbleCreatePoolInput.from_dict(nimble_create_pool_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


