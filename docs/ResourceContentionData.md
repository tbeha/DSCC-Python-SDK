# ResourceContentionData

Resource contention per resource response structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_metric_data** | [**List[HistoricalData]**](HistoricalData.md) |  | [optional] 
**top_contributors** | [**List[ResourceContentionContributors]**](ResourceContentionContributors.md) |  | [optional] 

## Example

```python
from dscc.models.resource_contention_data import ResourceContentionData

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceContentionData from a JSON string
resource_contention_data_instance = ResourceContentionData.from_json(json)
# print the JSON string representation of the object
print(ResourceContentionData.to_json())

# convert the object into a dict
resource_contention_data_dict = resource_contention_data_instance.to_dict()
# create an instance of ResourceContentionData from a dict
resource_contention_data_from_dict = ResourceContentionData.from_dict(resource_contention_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


