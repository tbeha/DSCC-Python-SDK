# NimbleInitiatorReview

initiator review

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | address | [optional] 
**changes** | [**NimbleChanges**](NimbleChanges.md) |  | [optional] 

## Example

```python
from dscc.models.nimble_initiator_review import NimbleInitiatorReview

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleInitiatorReview from a JSON string
nimble_initiator_review_instance = NimbleInitiatorReview.from_json(json)
# print the JSON string representation of the object
print(NimbleInitiatorReview.to_json())

# convert the object into a dict
nimble_initiator_review_dict = nimble_initiator_review_instance.to_dict()
# create an instance of NimbleInitiatorReview from a dict
nimble_initiator_review_from_dict = NimbleInitiatorReview.from_dict(nimble_initiator_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


