# NimbleHostReview

host review

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**NimbleChanges**](NimbleChanges.md) |  | [optional] 
**initiators** | [**List[NimbleInitiatorReview]**](NimbleInitiatorReview.md) | list of initiator reviews | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from dscc.models.nimble_host_review import NimbleHostReview

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleHostReview from a JSON string
nimble_host_review_instance = NimbleHostReview.from_json(json)
# print the JSON string representation of the object
print(NimbleHostReview.to_json())

# convert the object into a dict
nimble_host_review_dict = nimble_host_review_instance.to_dict()
# create an instance of NimbleHostReview from a dict
nimble_host_review_from_dict = NimbleHostReview.from_dict(nimble_host_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


