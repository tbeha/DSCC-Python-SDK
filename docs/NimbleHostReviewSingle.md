# NimbleHostReviewSingle

Provisioning review response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_group_id** | **str** | Host group ID | [optional] 
**hosts** | [**List[NimbleHostReview]**](NimbleHostReview.md) | list of hosts | [optional] 

## Example

```python
from dscc.models.nimble_host_review_single import NimbleHostReviewSingle

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleHostReviewSingle from a JSON string
nimble_host_review_single_instance = NimbleHostReviewSingle.from_json(json)
# print the JSON string representation of the object
print(NimbleHostReviewSingle.to_json())

# convert the object into a dict
nimble_host_review_single_dict = nimble_host_review_single_instance.to_dict()
# create an instance of NimbleHostReviewSingle from a dict
nimble_host_review_single_from_dict = NimbleHostReviewSingle.from_dict(nimble_host_review_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


