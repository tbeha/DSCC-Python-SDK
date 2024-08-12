# NimblecapacityHistory

capacity performance trends for given granularity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | count of series data | [optional] 
**request_uri** | **str** | requestUri for detailed storage object | [optional] 
**series_data** | [**List[NimblecapacitySeriesData]**](NimblecapacitySeriesData.md) |  | [optional] 

## Example

```python
from dscc.models.nimblecapacity_history import NimblecapacityHistory

# TODO update the JSON string below
json = "{}"
# create an instance of NimblecapacityHistory from a JSON string
nimblecapacity_history_instance = NimblecapacityHistory.from_json(json)
# print the JSON string representation of the object
print(NimblecapacityHistory.to_json())

# convert the object into a dict
nimblecapacity_history_dict = nimblecapacity_history_instance.to_dict()
# create an instance of NimblecapacityHistory from a dict
nimblecapacity_history_from_dict = NimblecapacityHistory.from_dict(nimblecapacity_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


