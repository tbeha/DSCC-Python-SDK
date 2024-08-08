# NimbleInitiatorsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NimbleInitiator]**](NimbleInitiator.md) |  | [optional] 
**page_limit** | **int** | page limit | [optional] 
**page_offset** | **int** | page offset | [optional] 
**request_uri** | **str** | requestUri for nimble initiator objects | [optional] 
**total** | **int** | Total number of initiators. | [optional] 

## Example

```python
from dscc.models.nimble_initiators_list import NimbleInitiatorsList

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleInitiatorsList from a JSON string
nimble_initiators_list_instance = NimbleInitiatorsList.from_json(json)
# print the JSON string representation of the object
print(NimbleInitiatorsList.to_json())

# convert the object into a dict
nimble_initiators_list_dict = nimble_initiators_list_instance.to_dict()
# create an instance of NimbleInitiatorsList from a dict
nimble_initiators_list_from_dict = NimbleInitiatorsList.from_dict(nimble_initiators_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


