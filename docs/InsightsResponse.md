# InsightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[InsightsData]**](InsightsData.md) |  | [optional] 

## Example

```python
from dscc.models.insights_response import InsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsResponse from a JSON string
insights_response_instance = InsightsResponse.from_json(json)
# print the JSON string representation of the object
print(InsightsResponse.to_json())

# convert the object into a dict
insights_response_dict = insights_response_instance.to_dict()
# create an instance of InsightsResponse from a dict
insights_response_from_dict = InsightsResponse.from_dict(insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


