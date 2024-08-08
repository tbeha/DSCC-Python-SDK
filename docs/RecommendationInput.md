# RecommendationInput

Request body for creating provisioning Workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_group_id** | **str** | host group id | [optional] 
**product_family** | **str** | Storage device type | [optional] 
**size_mib** | **int** | volume size requirement | 

## Example

```python
from dscc.models.recommendation_input import RecommendationInput

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationInput from a JSON string
recommendation_input_instance = RecommendationInput.from_json(json)
# print the JSON string representation of the object
print(RecommendationInput.to_json())

# convert the object into a dict
recommendation_input_dict = recommendation_input_instance.to_dict()
# create an instance of RecommendationInput from a dict
recommendation_input_from_dict = RecommendationInput.from_dict(recommendation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


