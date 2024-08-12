# NimbleWitnessesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleWitness]**](NimbleWitness.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | Request Uri for witness objects | [optional] 
**total** | **int** | Total number of witnesses. | [optional] 

## Example

```python
from dscc.models.nimble_witnesses_list import NimbleWitnessesList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleWitnessesList from a JSON string
nimble_witnesses_list_instance = NimbleWitnessesList.from_json(json)
# print the JSON string representation of the object
print(NimbleWitnessesList.to_json())

# convert the object into a dict
nimble_witnesses_list_dict = nimble_witnesses_list_instance.to_dict()
# create an instance of NimbleWitnessesList from a dict
nimble_witnesses_list_from_dict = NimbleWitnessesList.from_dict(nimble_witnesses_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


