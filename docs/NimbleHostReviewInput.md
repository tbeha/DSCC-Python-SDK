# NimbleHostReviewInput

Request body for provisioning review post call

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_groups** | **List[Optional[str]]** | list of host groups | [optional] 

## Example

```python
from dscc.models.nimble_host_review_input import NimbleHostReviewInput

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleHostReviewInput from a JSON string
nimble_host_review_input_instance = NimbleHostReviewInput.from_json(json)
# print the JSON string representation of the object
print(NimbleHostReviewInput.to_json())

# convert the object into a dict
nimble_host_review_input_dict = nimble_host_review_input_instance.to_dict()
# create an instance of NimbleHostReviewInput from a dict
nimble_host_review_input_from_dict = NimbleHostReviewInput.from_dict(nimble_host_review_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


