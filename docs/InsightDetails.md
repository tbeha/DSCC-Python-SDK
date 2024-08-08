# InsightDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_details** | **str** |  | [optional] 
**end_time** | **int** |  | [optional] 
**start_time** | **int** |  | [optional] 

## Example

```python
from dscc.models.insight_details import InsightDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InsightDetails from a JSON string
insight_details_instance = InsightDetails.from_json(json)
# print the JSON string representation of the object
print(InsightDetails.to_json())

# convert the object into a dict
insight_details_dict = insight_details_instance.to_dict()
# create an instance of InsightDetails from a dict
insight_details_from_dict = InsightDetails.from_dict(insight_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


